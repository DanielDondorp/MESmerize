"""
@author: kushal

Chatzigeorgiou Group
Sars International Centre for Marine Molecular Biology

GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007
"""

import os

# disable tf deprecation warnings
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import tensorflow as tf

tf.compat.v1.logging.set_verbosity(tf.compat.v1.logging.ERROR)

import tifffile
from matplotlib import pyplot as plt
import skimage
import numpy as np
import numexpr
from nuset import Nuset
from tqdm import tqdm
from typing import List, Tuple
from matplotlib import cm
from matplotlib.colors import LinearSegmentedColormap
from multiprocessing import Pool, cpu_count
from scipy.ndimage import label as label_image

from PyQt5 import QtWidgets, QtCore, QtGui
from qtap import Function
from ..core import ViewerUtils, ViewerWorkEnv
from ...pyqtgraphCore import GraphicsLayoutWidget, ImageItem, ViewBox
from ...pyqtgraphCore.console.Console import ConsoleWidget
from ...common.qdialogs import *
from ...common.configuration import console_history_path
from ...common.utils import HdfTools

cmap_magenta = LinearSegmentedColormap.from_list('magentas', [(0, 0, 0), (0,)*3, (1, 0, 1)])
cmap_cyan = LinearSegmentedColormap.from_list('cyans', [(0, 0, 0), (0,)*3, (0, 1, 1)])


def get_projection(img: np.ndarray, proj: str = 'std') -> np.ndarray:
    func = getattr(np, proj)

    return func(img, axis=2)


def get_preprocess(
        img: np.ndarray,
        do_preprocess: bool = True,
        do_sigmoid: bool = True,
        sigmoid_cutoff: float = 40.0,
        sigmoid_gain: float = 0.10,
        sigmoid_invert: bool = False,
        do_equalize: bool = True,
        equalize_kernel: int = 8,
) -> np.ndarray:
    """

    :param img: input image
    :param do_sigmoid: Perform sigmoid correction
    :param sigmoid_cutoff: sigmoid cutoff
    :param sigmoid_gain: sigmoid gain
    :param sigmoid_invert: invert after sigmoid correction (necessary sometimes)
    :param do_equalize: Perform histogram equalization
    :param equalize_kernel: Size of equalization kernel
    :return: preprocessed image
    """
    if not do_preprocess:
        return normalize_image(img, np.float32)

    img = img.astype(np.float32)

    if do_sigmoid:
        img = skimage.exposure.adjust_sigmoid(
            img,
            cutoff=sigmoid_cutoff,
            gain=sigmoid_gain,
            inv=sigmoid_invert
        )

    if do_equalize:
        # equalize_hist works more easily with 16 bit integers
        img = normalize_image(img, np.uint16)
        img = skimage.exposure.equalize_adapthist(img, kernel_size=equalize_kernel)

    # float32 is best for GPU I think?
    img = normalize_image(img, np.float32)

    return img


def wrap_preprocess(kwargs):
    return get_preprocess(**kwargs)


# from NuSeT processing cleanimage function
def get_postprocess(
        img: np.ndarray,
        do_postprocess: bool = False,
        abs_obj_threshold: int = -1,
        rel_obj_threshold: int = 5,
        obj_connectivity: int = 2,
        abs_hol_threshold: int = -1,
        rel_hol_threshold: int = 5,
        hol_connectivity: int = 2
    ) -> np.ndarray:

    if not do_postprocess:
        return img

    if not img.size > 0:
        return img

    image = img.astype(np.bool)
    im_label = skimage.morphology.label(image, connectivity=1)
    num_cells = np.max(im_label)
    mean_area = np.sum(image).astype(np.float32) / num_cells

    if abs_obj_threshold == -1:
        min_obj_size = mean_area / rel_obj_threshold
    else:
        min_obj_size = abs_obj_threshold
    image = skimage.morphology.remove_small_objects(image, min_size=min_obj_size, connectivity=obj_connectivity)

    if abs_hol_threshold == -1:
        min_hol_size = mean_area / rel_hol_threshold
    else:
        min_hol_size = abs_hol_threshold
    image = skimage.morphology.remove_small_holes(image, min_size=min_hol_size, connectivity=hol_connectivity)

    return image.astype(np.uint8)


# adapted from https://github.com/ver228/tierpsy-tracker/blob/master/tierpsy/analysis/compress/compressVideo.py
def normalize_image(img, dtype):
    # normalise image intensities between 0 and the max range of the dtype
    imax = (img.max() + np.abs(img.min())).astype(dtype)
    # we will set the values between 0 and max value of the float/int type
    imin = 0

    # max value of the dtype
    if np.issubdtype(dtype, np.floating):
        factor = (np.finfo(dtype).max - 1) / (imax - imin)
    elif np.issubdtype(dtype, np.integer):
        factor = (np.iinfo(dtype).max - 1) / (imax - imin)

    imgN = numexpr.evaluate('(img-imin)*factor')
    imgN = imgN.astype(dtype)

    return imgN


# adapted from https://github.com/flatironinstitute/CaImAn/blob/master/caiman/base/rois.py#L88
def get_sparse_mask(segmented_img: np.ndarray, raw_img_shape: tuple):
    # allocate array with same size as the raw input image
    # so that the dims match for CNMF
    img = np.zeros(raw_img_shape, dtype=segmented_img.dtype)

    # fill the allocated array with vals from the NuSeT segmentation
    # sometimes the segmented image has its dims trimmed by a few pixels
    if len(raw_img_shape) == 3:
        img[:, :segmented_img.shape[1], :segmented_img.shape[2]] = segmented_img
    else:
        img[:segmented_img.shape[0], :segmented_img.shape[1]] = segmented_img

    areas = label_image(img)
    A = np.zeros((np.prod(img.shape), areas[1]), dtype=bool)

    selem: np.array = np.ones((3,)*len(segmented_img.shape))

    print("Creating sparse matrix, this could take a while...")
    for i in tqdm(range(areas[1])):
        temp = (areas[0] == i + 1)
        temp = skimage.morphology.closing(temp, selem=selem)

        A[:, i] = temp.flatten('F')

    return A


class ModuleGUI(QtWidgets.QMainWindow):
    def __init__(self, parent, viewer_ref):
        QtWidgets.QMainWindow.__init__(self)

        self.resize(1000, 900)
        self.menubar = self.menuBar()
        # self.setMenuBar(self.menubar)
        # self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 900))
        # self.menubar.setObjectName("menubar")


        self.widget = NusetWidget(self, viewer_ref)

        self.setCentralWidget(self.widget)

        self.dock_console = QtWidgets.QDockWidget(self)
        self.dock_console.setFeatures(
            QtWidgets.QDockWidget.DockWidgetFloatable | QtWidgets.QDockWidget.DockWidgetMovable
        )
        # self.dockWidgetContents = QtWidgets.QWidget()
        # self.dock_console.setWidget(self.dockWidgetContents)
        self.addDockWidget(QtCore.Qt.BottomDockWidgetArea, self.dock_console)
        self.dock_console.hide()

        histfile = os.path.join(console_history_path, 'nuset_widget.pik')
        self.console_widget = ConsoleWidget(
            parent=self, namespace={'this': self.widget}, historyFile=histfile
        )
        self.dock_console.setWidget(self.console_widget)
        self.dock_console.setWindowTitle("Console")
        self.dock_console.hide()

        self.menu_export = self.menubar.addMenu('&Export')

        self.action_export_cnmf_seeds = QtWidgets.QAction(text='CNMF seeds')
        self.action_export_cnmf_seeds.setToolTip(
            "Export as sparse matrix that can be used for \n"
            "seeding spatial components in Caiman CNMF"
        )
        self.menu_export.addAction(self.action_export_cnmf_seeds)

        self.action_export_viewer = QtWidgets.QAction("Manual ROIs - Viewer")
        self.menu_export.addAction(self.action_export_viewer)
        self.action_export_viewer.setToolTip(
            "Export as Manual ROIs into the Viewer"
        )

        self.menu_view = self.menubar.addMenu('&View')

        self.action_view_console = QtWidgets.QAction(text="Console")
        self.menu_view.addAction(self.action_view_console)
        self.action_view_console.setText("Console")
        self.action_view_console.setCheckable(True)
        self.action_view_console.setChecked(False)

        self.action_view_console.toggled.connect(
            lambda: self.dock_console.setVisible(
                self.action_view_console.isChecked()
            )
        )

        self.action_export_cnmf_seeds.triggered.connect(self.widget.save_masks)


class NusetWidget(QtWidgets.QWidget):
    def __init__(self, parent, viewer_ref):
        self.vi = ViewerUtils(viewer_ref)
        QtWidgets.QWidget.__init__(self, parent)

        self.vlayout = QtWidgets.QVBoxLayout(self)

        self.splitter = QtWidgets.QSplitter(QtCore.Qt.Horizontal)
        self.vlayout.addWidget(self.splitter)

        self.left_layout = QtWidgets.QVBoxLayout(self)

        self.left_widget = QtWidgets.QWidget(self.splitter)
        self.left_widget.setLayout(self.left_layout)

        hlayout_custom_img = QtWidgets.QHBoxLayout(self.left_widget)
        self.lineedit_custom_img_path = QtWidgets.QLineEdit(self.left_widget)
        self.lineedit_custom_img_path.setPlaceholderText("Path to custom image or stack")
        self.lineedit_custom_img_path.setToolTip(
            "Use a different image or stack for segmentation, such as an image or stack of nuclei."
        )
        self.button_use_custom = QtWidgets.QPushButton(self.left_widget)
        self.button_use_custom.setMaximumWidth(50)
        self.button_use_custom.setText("Set")
        hlayout_custom_img.addWidget(self.lineedit_custom_img_path)
        hlayout_custom_img.addWidget(self.button_use_custom)
        self.left_layout.addLayout(hlayout_custom_img)

        hlayout_projection_radios = QtWidgets.QHBoxLayout(self.left_widget)
        self.radio_std = QtWidgets.QRadioButton(self.left_widget)
        self.radio_std.setText("Std. Deviation")
        self.radio_max = QtWidgets.QRadioButton(self.left_widget)
        self.radio_max.setText("Max")
        self.radio_mean = QtWidgets.QRadioButton(self.left_widget)
        self.radio_mean.setText("Mean")

        self.projection_option: str = ''

        for w in [self.radio_std, self.radio_max, self.radio_mean]:
            hlayout_projection_radios.addWidget(w)
            w.clicked.connect(self.update_projection)

        label_projections = QtWidgets.QLabel(self.left_widget)
        label_projections.setText("Choose Input Projection")
        label_projections.setStyleSheet("font-weight: bold")

        self.left_layout.addWidget(label_projections)
        self.left_layout.addLayout(hlayout_projection_radios)

        # projection image
        self.glw_raw = GraphicsLayoutWidget(self.left_widget)
        self.imgitem_raw = ImageItem()
        self.viewbox_raw = self.glw_raw.addViewBox()
        self.viewbox_raw.setAspectLocked(True)
        self.viewbox_raw.addItem(self.imgitem_raw)

        self.left_layout.addWidget(self.glw_raw)

        hlayout_preprocess = QtWidgets.QHBoxLayout(self.left_widget)

        arg_opts_preprocess = \
            {
                'img': {'ignore': True},

                'sigmoid_gain': {
                    'step': 0.01
                }
            }

        self.preprocess_controls = \
            Function(
                get_preprocess,
                arg_opts=arg_opts_preprocess,
                parent=self.left_widget
            )
        self.preprocess_controls.button_set.hide()
        self.preprocess_controls.sig_changed.connect(self.update_preprocess)
        self.preprocess_controls.set_title("Pre-process Settings")

        hlayout_preprocess.addWidget(self.preprocess_controls.widget)

        self.zslider = QtWidgets.QSlider(parent=self.left_widget, orientation=QtCore.Qt.Vertical)
        self.zslider.setInvertedAppearance(True)
        self.zslider.setSingleStep(1)
        self.zslider.valueChanged.connect(self.update_zlevel)

        label_zslider = QtWidgets.QLabel(self.left_widget)
        label_zslider.setText("z-level")

        self.spinbox_zlevel = QtWidgets.QSpinBox(self.left_widget)
        self.spinbox_zlevel.setSingleStep(1)
        self.spinbox_zlevel.valueChanged.connect(self.zslider.setValue)
        self.zslider.valueChanged.connect(self.spinbox_zlevel.setValue)


        hlayout_preprocess.addWidget(label_zslider)
        hlayout_preprocess.addWidget(self.zslider)
        hlayout_preprocess.addWidget(self.spinbox_zlevel)

        self.left_layout.addLayout(hlayout_preprocess)

        # preprocess image item
        self.glw_preprocess = GraphicsLayoutWidget(self.left_widget)
        self.imgitem_preprocess = ImageItem()
        self.viewbox_preprocess = self.glw_preprocess.addViewBox()
        self.viewbox_preprocess.setAspectLocked(True)
        self.viewbox_preprocess.addItem(self.imgitem_preprocess)

        self.left_layout.addWidget(self.glw_preprocess)

        self.splitter.addWidget(self.left_widget)

        # segmentation stuff
        self.nuset_model = Nuset()

        self.right_layout = QtWidgets.QVBoxLayout(self)

        self.right_widget = QtWidgets.QWidget(self.splitter)
        self.right_widget.setLayout(self.right_layout)

        hlayout_nuset = QtWidgets.QHBoxLayout(self.right_widget)

        arg_opts_nuset = \
            {
                'image': {'ignore': True},

                'min_score': {
                    'minmax': (0.0, 1.0),
                    'step': 0.05
                },

                'nms_threshold': {
                    'minmax': (0.0, 1.0),
                    'step': 0.05
                },

                'rescale_ratio': {
                    'minmax': (0.1, 10.0),
                    'step': 0.5,
                    'val': 1.1  # not working if set to 1.0 with pyqtgraph ImageItem for some reason
                }

            }

        self.nuset_controls = \
            Function(
                self.nuset_model.predict,
                arg_opts=arg_opts_nuset,
                parent=self.right_widget
            )

        # self.nuset_controls.button_set.hide()
        self.nuset_controls.sig_set_clicked.connect(self.update_segmentation)
        self.nuset_controls.set_title("NuSeT Parameters")
        hlayout_nuset.addWidget(self.nuset_controls.widget)

        arg_opts_postprocess = \
            {
                'img': {'ignore': True},

                'abs_obj_threshold': {
                    'minmax': (-1, 100),
                    'step': 2,
                },

                'rel_obj_threshold': {
                    'minmax': (0, 100),
                    'step': 2
                },

                'obj_connectivity': {
                    'minmax': (0, 10),
                    'step': 1
                },

                'abs_hol_threshold': {
                    'minmax': (-1, 100),
                    'step': 2,
                },

                'rel_hol_threshold': {
                    'minmax': (0, 100),
                    'step': 2
                },

                'hol_connectivity': {
                    'minmax': (0, 100),
                    'step': 1
                }
            }

        self.postprocess_controls = \
            Function(
                get_postprocess,
                arg_opts=arg_opts_postprocess,
                parent=self.right_widget
            )
        self.postprocess_controls.button_set.hide()
        self.postprocess_controls.sig_changed.connect(self.update_postprocess)
        self.postprocess_controls.set_title("Post-process Parameters")

        hlayout_nuset.addWidget(self.postprocess_controls.widget)
        self.right_layout.addLayout(hlayout_nuset)

        self.checkbox_segment_current_plane = QtWidgets.QCheckBox(self.nuset_controls.widget)
        self.checkbox_segment_current_plane.setText("Only segment current plane")
        self.checkbox_segment_current_plane.setToolTip(
            "Performs segmentation for only the current plane, "
            "useful for trying out parameters."
        )
        self.checkbox_segment_current_plane.setChecked(True)
        self.nuset_controls.vlayout.addWidget(self.checkbox_segment_current_plane)

        self.glw_segmented = GraphicsLayoutWidget(self.right_widget)
        self.imgitem_segmented = ImageItem()
        self.imgitem_segmented_underlay = ImageItem()
        self.viewbox_segmented = self.glw_segmented.addViewBox()
        self.viewbox_segmented.setAspectLocked(True)
        self.viewbox_segmented.addItem(self.imgitem_segmented)
        self.viewbox_segmented.addItem(self.imgitem_segmented_underlay)

        # colormaps for the mask overlay plot
        cm_cyan = cm.get_cmap(cmap_cyan)
        cm_cyan._init()
        lut_cyan = (cm_cyan._lut * 255).view(np.ndarray)[128:-5]
        self.imgitem_segmented_underlay.setLookupTable(lut_cyan)

        # colormaps for the mask overlay plot
        cm_magenta = cm.get_cmap(cmap_magenta)
        cm_magenta._init()
        lut_magenta = (cm_magenta._lut * 255).view(np.ndarray)[:-5]  # so it displays as a mask
        self.imgitem_segmented.setLookupTable(lut_magenta)

        # allow transparency
        # self.imgitem_segmented.setCompositionMode(QtGui.QPainter.CompositionMode_Overlay)
        self.imgitem_segmented_underlay.setCompositionMode(QtGui.QPainter.CompositionMode_SourceOver)

        self.imgitem_segmented.setZValue(2)
        self.imgitem_segmented.setOpacity(0.5)
        self.imgitem_segmented_underlay.setZValue(1)
        self.imgitem_segmented_underlay.setOpacity(0.3)

        self.slider_underlay_opacity = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        self.slider_underlay_opacity.setMinimum(0)
        self.slider_underlay_opacity.setMaximum(100)
        self.slider_underlay_opacity.setValue(30)
        self.slider_underlay_opacity.valueChanged.connect(
            lambda v: self.imgitem_segmented_underlay.setOpacity(v / 100)
        )
        label_underlay_opacity = QtWidgets.QLabel(self.nuset_controls.widget)
        label_underlay_opacity.setText("Underlay opacity")
        self.nuset_controls.vlayout.addWidget(label_underlay_opacity)
        self.nuset_controls.vlayout.addWidget(self.slider_underlay_opacity)

        self.slider_mask_opacity = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        self.slider_mask_opacity.setMinimum(0)
        self.slider_mask_opacity.setMaximum(100)
        self.slider_mask_opacity.setValue(50)
        self.slider_mask_opacity .valueChanged.connect(
            lambda v: self.imgitem_segmented.setOpacity(v / 100)
        )
        label_segmented_opacity = QtWidgets.QLabel(self.nuset_controls.widget)
        label_segmented_opacity.setText("Segmentation opacity")
        self.nuset_controls.vlayout.addWidget(label_segmented_opacity)
        self.nuset_controls.vlayout.addWidget(self.slider_mask_opacity)

        self.combo_blend_mode = QtWidgets.QComboBox(self.nuset_controls.widget)
        self.combo_blend_mode.addItems(
            [
                'SourceOver',
                'Overlay',
                'Plus',
                'Multiply'
            ]
        )
        self.combo_blend_mode.setCurrentIndex(0)
        self.combo_blend_mode.currentTextChanged.connect(
            lambda opt: self.imgitem_segmented.setCompositionMode(
                getattr(QtGui.QPainter, f'CompositionMode_{opt}')
            )
        )
        label_blend_mode = QtWidgets.QLabel(self.nuset_controls.widget)
        label_blend_mode.setText('Blend mode:')
        self.nuset_controls.vlayout.addWidget(label_blend_mode)
        self.nuset_controls.vlayout.addWidget(self.combo_blend_mode)

        self.right_layout.addWidget(self.glw_segmented)
        self.splitter.addWidget(self.right_widget)

        self.imgs_projected: List[np.ndarray] = []
        self.imgs_preprocessed: List[np.ndarray] = []
        self.imgs_segmented: List[np.ndarray] = []
        self.imgs_postprocessed: List[np.ndarray] = []

        self.input_img: np.ndarray = np.empty(0)
        self.zlevel = 0
        self.z_max: int = 0

        self.vi.sig_workEnv_changed.connect(self.set_input)

        self.process_pool = Pool(cpu_count())

        self.error_label = QtWidgets.QLabel(self)
        self.error_label.setMaximumHeight(20)
        self.error_label.setStyleSheet("font-weight: bold; color: red")
        self.vlayout.addWidget(self.error_label)

        self.projection_option = ''
        self.params_final = None

    def set_input(self, workEnv: ViewerWorkEnv):
        self.clear_widget()

        try:
            self.input_img = workEnv.imgdata._seq
        except:
            return

        if workEnv.imgdata.z_max is None:
            self.z_max = 0
        else:
            self.z_max = workEnv.imgdata.z_max

        self.zslider.valueChanged.disconnect(self.update_zlevel)
        self.zslider.setValue(0)
        self.zslider.setMaximum(self.z_max)
        self.spinbox_zlevel.setMaximum(self.z_max)
        self.zslider.valueChanged.connect(self.update_zlevel)

    def update_zlevel(self, z: int):
        self.zlevel = z

        for imgitem, imglist in zip(
            [
                self.imgitem_raw,
                self.imgitem_preprocess,
                self.imgitem_segmented_underlay,
                self.imgitem_segmented
            ],
            [
                self.imgs_projected,
                self.imgs_preprocessed,
                self.imgs_preprocessed,
                self.imgs_postprocessed
            ]
        ):
            if imglist:  # set if the list is not empty
                if imglist[z].size > 0:
                    imgitem.setImage(imglist[z])

    def update_projection(self):
        if not self.input_img.size > 0:
            self.error_label.setText("No input image")
            return

        if self.radio_std.isChecked():
            opt = 'std'
        elif self.radio_max.isChecked():
            opt = 'max'
        elif self.radio_mean.isChecked():
            opt = 'mean'

        if self.projection_option == opt:
            return

        func = getattr(np, opt)

        print("Updating Projection(s)")
        if self.input_img.ndim == 4:
            self.imgs_projected = [func(self.input_img[:, :, :, z], axis=2) for z in tqdm(self.z_max)]
        else:
            self.imgs_projected = [func(self.input_img, axis=2)]

    def update_preprocess(self, params):
        if not self.imgs_projected:
            self.error_label.setText("Projection Image is Empty")
            return

        print("Preprocessing Image(s)")

        # self.image_preprocesses = [
        #     get_preprocess(p, **params) for p in tqdm(self.image_projections)
        # ]

        kwargs = [{'img': img, **params} for img in self.imgs_projected]

        self.imgs_preprocessed = self.process_pool.map(wrap_preprocess, kwargs)

        self.imgitem_preprocess.setImage(self.imgs_preprocessed[self.zlevel])
        self.imgitem_segmented_underlay.setImage(self.imgs_preprocessed[self.zlevel])
        self.error_label.clear()

    def update_segmentation(self, params):
        if not self.imgs_preprocessed:
            self.error_label.setText("Preprocess Image is Empty")
            return

        print("Segmenting Image(s)")
        if not self.checkbox_segment_current_plane.isChecked():
            self.imgs_segmented = [
                self.nuset_model.predict(img, **params) for img in tqdm(self.imgs_preprocessed)
            ]
        else:
            self.imgs_segmented = [
                np.empty(0) for i in range(self.z_max + 1)
            ]

            self.imgs_segmented[self.zlevel] = self.nuset_model.predict(
                self.imgs_preprocessed[self.zlevel], **params
            )

        # postprocess funciton will just return the segmented img if do_postprocess is False
        self.update_postprocess(self.postprocess_controls.get_data())

        self.params_final = \
            {
                'method': 'NuSeT',
                'projection_option': self.projection_option,
                **self.preprocess_controls.get_data(),
                **self.nuset_controls.get_data(),
                **self.postprocess_controls.get_data(),
            }

        self.error_label.clear()

    def update_postprocess(self, params):
        if not self.imgs_segmented:
            self.error_label.setText("Segmented Image is Empty")
            return

        print("Postprocessing Image(s)")
        self.imgs_postprocessed = [
            get_postprocess(img, **params) for img in tqdm(self.imgs_segmented)
        ]

        self.imgitem_segmented.setImage(self.imgs_postprocessed[self.zlevel])
        self.error_label.clear()

    def clear_widget(self):
        self.imgs_projected.clear()
        self.imgs_preprocessed.clear()
        self.imgs_segmented.clear()
        self.imgs_postprocessed.clear()

        self.imgitem_raw.clear()
        self.imgitem_preprocess.clear()
        self.imgitem_segmented.clear()
        self.imgitem_segmented_underlay.clear()

        self.radio_std.setChecked(False)
        self.radio_max.setChecked(False)
        self.radio_mean.setChcked(False)

        self.projection_option = ''

    @use_save_file_dialog('Save masks', None, '.h5')
    @present_exceptions()
    def save_masks(self, path, *args):
        if not self.imgs_segmented:
            raise ValueError("You must segment images before you can proceed.")

        for img in self.imgs_segmented:
            if not img.size > 0:
                raise ValueError("Your must segment the entire stack before you can proceed.")

        if QtWidgets.QMessageBox.question(
            self, 'Export for CNMF?', 'This may take a few minutes, and could take ~30 minutes '
                                      'if segmenting a large 3D stack. Proceed?',
            ) == QtWidgets.QMessageBox.No:
            return

        if self.z_max > 0:
            seg_img = np.stack(self.imgs_segmented)
            shape = np.stack(self.imgs_projected).shape

        else:
            seg_img = self.imgs_segmented[0].T
            shape = self.imgs_projected[0].T.shape

        Ain = get_sparse_mask(seg_img, shape)

        d = {'sparse_mask': Ain, 'segment_params': self.params_final}
        HdfTools.save_dict(d, path, 'data')