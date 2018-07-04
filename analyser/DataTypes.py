#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 2018

@author: kushal

Chatzigeorgiou Group
Sars International Centre for Marine Molecular Biology

GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007
"""

import pandas as pd
import numpy as np
import pickle
from copy import deepcopy
from uuid import uuid4


class BaseTransmission:
    def __init__(self, df: pd.DataFrame, src: list, **kwargs):
        """
        Base class for common Transmission functions

        :param  src:    List of dicts with history of the nodes & node parameters
                        the transmission has been processed through

        Some optional kwargs:
        :param  STIM_DEFS:  STIM_DEF columns, used by the AlignStims control node for example
        :type   STIM_DEFS:  list

        :param  ROI_DEFS:   ROI_DEF columns, used by the ROI selection control node for example
        :type   ROI_DEFS:   list
        """
        self.df = df
        self.src = src
        self.kwargs = kwargs
        self.kwargs_keys = list(kwargs.keys())

        for key in self.kwargs_keys:
            setattr(self, key, kwargs[key])

    @classmethod
    def from_pickle(cls, path):
        """
        :param path: Path to the pickle file
        :return: Transmission class object
        """
        p = pickle.load(open(path, 'rb'))
        return cls(**p)

    def _make_dict(self) -> dict:
        """
        Package attributes as a dict, useful for pickling
        """
        d = {'df':  self.df,
             'src': self.src}

        for key in self.kwargs_keys:
            d.update({key: getattr(self, key)})
        return d

    def to_pickle(self, path: str):
        """
        :param path: Path of where to store pickle
        """
        pickle.dump(self._make_dict(), open(path, 'wb'), protocol=4)

    def copy(self):
        return deepcopy(self)

    @classmethod
    def empty_df(cls, transmission, addCols=[]):
        """
        :param transmission: Transmission object
        :param addCols: list of columns to add
        :return: empty DataFrame with the columns in this Transmission's dataframe along with any additional columns
        that were specified.
        """
        c = list(transmission.df.columns) + addCols
        e_df = pd.DataFrame(columns=c)
        return cls(e_df, transmission.src, **transmission.kwargs)


class Transmission(BaseTransmission):
    """The regular transmission class used throughout the flowchart"""
    @classmethod
    def from_proj(cls, proj_path: str, dataframe: pd.DataFrame, df_name='', misc_info=None):
        """
        :param proj_path: root directory of the project
        :param dataframe: Chosen Child DataFrame from the Mesmerize Project
        :param df_name:   name of dataframe, usually the project browswer tab indicating the child dataframe name

        :return: Transmission class object
        """
        df = dataframe.copy()
        df[['curve', 'meta', 'stim_maps']] = df.apply(lambda r: Transmission._load_files(proj_path, r), axis=1)
        df['raw_curve'] = df['curve']
        
        try:
            from common import configuration
            stim_defs = configuration.proj_cfg.options('STIM_DEFS')
            roi_defs = configuration.proj_cfg.options('ROI_DEFS')
        except:
            return cls(df, src=[{'raw': df_name}])

        return cls(df, src=[{'raw': df_name}], STIM_DEFS=stim_defs, ROI_DEFS=roi_defs, misc_info=misc_info)

    @staticmethod
    def _load_files(proj_path: str, row: pd.Series) -> pd.Series:
        """Loads npz and pickle files of Curves & Img metadata according to the paths specified in each row of the
        chosen child DataFrame in the project"""

        path = proj_path + row['CurvePath']
        npz = np.load(path)
#        print(npz.f.curve[1])

        pikPath = proj_path + row['ImgInfoPath']
        pik = pickle.load(open(pikPath, 'rb'))
        meta = pik['meta']
        stim_maps = pik['stim_maps']
        
        return pd.Series({'curve': npz.f.curve[1], 'meta': meta, 'stim_maps': [[stim_maps]]})

    # @classmethod
    # def empty_df(cls, transmission, addCols=[]):
    #     """
    #     :return: Same transmission with dataframe containing empty rows (columns preserved)
    #     """
    #     c = list(transmission.df.columns) + addCols
    #     e_df = pd.DataFrame(columns=c)
    #     return cls(e_df, src=transmission.src,
    #                STIM_DEFS=transmission.STIM_DEFS,
    #                ROI_DEFS=transmission.ROI_DEFS)


class GroupTransmission(BaseTransmission):
    """Transmission class for setting groups to individual transmissions that can later be merged into a single
    StatsTransmission"""
    @classmethod
    def from_ca_data(cls, transmission: Transmission, groups_list: list):
        """
        :param  transmission: Raw Transmission object
        :param  groups_list: List of groups to which the raw Transmission object belongs

        :return: GroupTransmission
        """
        if not (any('Peak_Features' in d for d in transmission.src) or
                    any('AlignStims' in d for d in transmission.src)):
            raise IndexError('No Peak Features or Stimulus Alignment data to group the data.')

        t = transmission.copy()

        t.df, groups_list = GroupTransmission._append_group_bools(t.df, groups_list)

        # gid = uuid4()
        #
        # t.df['uuid'] = gid

        t.src.append({'Grouped': ', '.join(groups_list)})

        return cls(t.df, t.src, groups_list=groups_list)

    @classmethod
    def from_behav_data(cls, transmission: Transmission, groups_list: list):
        raise NotImplementedError

    @staticmethod
    def _append_group_bools(df: pd.DataFrame, groups_list: list) -> (pd.DataFrame, list):
        """
        :param df:
        :param groups_list:
        :return:
        """
        new_gl = []
        for group in groups_list:
            group = '_G_' + group
            new_gl.append(group)
            df[group] = True

        return df, new_gl


class StatsTransmission(BaseTransmission):
    """Transmission class that contains a DataFrame consisting of data from many groups. Columns with names that start
    with '_G_' denote groups. Booleans indicate whether or not that row belong to that group."""
    @classmethod
    def from_group_trans(cls, transmissions: list):
        """
        :param transmissions list of GroupTransmission objects
        """
        all_groups = []
        for tran in transmissions:
            assert isinstance(tran, GroupTransmission)
            all_groups += tran.groups_list

        all_groups = list(set(all_groups))

        all_dfs = []
        all_srcs = []
        for tran in transmissions:
            tran = tran.copy()
            assert isinstance(tran, GroupTransmission)
            for group in all_groups:
                if group in tran.groups_list:
                    tran.df[group] = True
                else:
                    tran.df[group] = False
            all_srcs.append(tran.src)
            all_dfs.append(tran.df)

        all_groups = list(set(all_groups))

        df = pd.concat(all_dfs)
        assert isinstance(df, pd.DataFrame)
        df.reset_index()

        return cls(df, all_srcs, all_groups=all_groups)

    @classmethod
    def merge(cls, transmissions):
        """
        :param  transmissions: Transmission objects
        :type   transmissions: GroupTransmission, StatsTransmission

        :return: StatsTransmission
        """
        groups = []
        stats = []
        all_srcs = []
        all_groups = []

        for t in transmissions:
            if isinstance(t, GroupTransmission):
                groups.append(t)

            elif isinstance(t, StatsTransmission):
                stats.append(t)
                all_srcs.append(t.src)
                all_groups.append(t.all_groups)
            else:
                e = type(t)
                raise TypeError("Cannot merge type: '" + str(e) + "'\n"
                                "You must only pass GroupTransmission or StatsTransmission objects.")

        g_merge = StatsTransmission.from_group_trans(groups)

        all_groups = list(set(all_groups + g_merge.all_groups))

        all_srcs = all_srcs + g_merge.all_srcs

        all_dfs = [g_merge] + stats

        df = pd.concat(all_dfs)
        return cls(df, all_srcs, all_groups=all_groups)
