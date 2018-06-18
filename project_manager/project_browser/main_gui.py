#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on June 17 2018

@author: kushal

Chatzigeorgiou Group
Sars International Centre for Marine Molecular Biology

GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007
"""

from PyQt5 import QtCore, QtGui, QtWidgets
from .tab_area_widget import TabAreaWidget
import pandas as pd
from common import configuration
from misc_widgets.list_widget_dialog import ListWidgetDialog
from functools import partial
from viewer.core.common import ViewerInterface
from viewer.core.viewer_work_environment import ViewerWorkEnv
from common.window_manager import WindowClass
from common import start


class ProjectBrowserGUI(QtWidgets.QWidget):
    def __init__(self, parent, dataframe: pd.DataFrame):
        QtWidgets.QWidget.__init__(self)

        self.tabs = {}
        self.dataframe = dataframe

        self.vertical_layout = QtWidgets.QVBoxLayout(self)

        self.tab_widget = QtWidgets.QTabWidget()
        self.vertical_layout.addWidget(self.tab_widget)

        self.add_tab(dataframe, [], is_root=True)

        self.tab_widget.tabCloseRequested.connect(self.close_tab)

    def add_tab(self, dataframe, filter_history, is_root=False):
        if not is_root:
            tab_name = QtWidgets.QInputDialog.getText(self, None, 'Enter name for new tab: ')
            if tab_name[0] == '' or tab_name[1] is False:
                return
            elif tab_name[0] in configuration.df_refs.keys():
                QtWidgets.QMessageBox.warning(self, 'DataFrame title already exists!',
                                              'That name already exists in your project, choose a different name!')
                self.add_tab(dataframe, filter_history, is_root)
            tab_name = tab_name[0]
        else:
            tab_name = 'root'

        tab_area_widget = TabAreaWidget(self.tab_widget, tab_name, dataframe, filter_history, is_root)
        tab_area_widget.signal_new_tab_requested.connect(self.slot_new_tab_requested)
        tab_area_widget.signal_open_sample_in_viewer_requested.connect(self.slot_open_sample_id_in_viewer)

        self.tab_widget.addTab(tab_area_widget, tab_name)

        self.tab_widget.setTabsClosable(True)
        bar = self.tab_widget.tabBar()
        bar.setTabButton(0, bar.RightSide, None)

        self.tabs.update({tab_name: tab_area_widget})

        if is_root:
            num_columns = len(tab_area_widget.columns)
            self.resize(min(1920, num_columns * 215), 400)

        self.tab_widget.setCurrentIndex(self.tab_widget.count() - 1)

    @QtCore.pyqtSlot(pd.DataFrame, list)
    def slot_new_tab_requested(self, dataframe, filter_history):
        print(dataframe)
        print(filter_history)
        self.add_tab(dataframe, filter_history)

    def close_tab(self, ix):
        pass

    @QtCore.pyqtSlot(str)
    def slot_open_sample_id_in_viewer(self, sample_id):
        viewers = configuration.window_manager.viewers

        if len(configuration.window_manager.viewers) == 0:
            start.viewer()

        elif len(configuration.window_manager.viewers) > 1:
            self.lwd = ListWidgetDialog()
            self.lwd.listWidget.addItems([str(i) for i in range(len(viewers))])
            self.lwd.label.setText('Viewer to show input in:')
            self.lwd.btnOK.clicked.connect(partial(self.open_sample_id_in_viewer, viewers, sample_id))
        else:
            self.open_sample_id_in_viewer(viewers[0], sample_id)

    def open_sample_id_in_viewer(self, viewers, sample_id):
        if not isinstance(viewers, WindowClass):
            viewer = viewers.viewer_reference
        else:
            if self.lwd.listWidget.currentItem() is None:
                QtWidgets.QMessageBox.warning(self, 'Nothing selected', 'You must select from the list')
                return
            i = int(self.lwd.listWidget.currentItem().data(0))
            viewer = viewers[i].viewer_reference

        vi = ViewerInterface(viewer_reference=viewer)

        row = self.dataframe[self.dataframe['SampleID'] == sample_id].iloc[0]
        pikPath = configuration.proj_path + row['ImgInfoPath']
        tiffPath = configuration.proj_path + row['ImgPath']

        if not vi.discard_workEnv():
            return

        vi.viewer.workEnv = ViewerWorkEnv.from_pickle(pikPath=pikPath, tiffPath=tiffPath)
        vi.update_workEnv()
        try:
            self.lwd.deleteLater()
        except:
            pass