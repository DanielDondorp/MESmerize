# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ImageViewTemplate.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1400, 980)
        self.gridLayout_2 = QtWidgets.QGridLayout(Form)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.splitter_3 = QtWidgets.QSplitter(Form)
        self.splitter_3.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_3.setObjectName("splitter_3")
        self.splitter_2 = QtWidgets.QSplitter(self.splitter_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitter_2.sizePolicy().hasHeightForWidth())
        self.splitter_2.setSizePolicy(sizePolicy)
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName("splitter_2")
        self.layoutWidget = QtWidgets.QWidget(self.splitter_2)
        self.layoutWidget.setObjectName("layoutWidget")
        self.FileMenusLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.FileMenusLayout.setContentsMargins(0, 0, 0, 0)
        self.FileMenusLayout.setObjectName("FileMenusLayout")
        self.openFileBtn = QtWidgets.QPushButton(self.layoutWidget)
        self.openFileBtn.setObjectName("openFileBtn")
        self.FileMenusLayout.addWidget(self.openFileBtn, 0, 0, 1, 1)
        self.mesfile_label = QtWidgets.QLabel(self.layoutWidget)
        self.mesfile_label.setObjectName("mesfile_label")
        self.FileMenusLayout.addWidget(self.mesfile_label, 1, 0, 1, 1)
        self.imgs_listw = QtWidgets.QListWidget(self.layoutWidget)
        self.imgs_listw.setEnabled(False)
        self.imgs_listw.setObjectName("imgs_listw")
        self.FileMenusLayout.addWidget(self.imgs_listw, 2, 1, 1, 1)
        self.progressBarLabel = QtWidgets.QLabel(self.layoutWidget)
        self.progressBarLabel.setText("")
        self.progressBarLabel.setObjectName("progressBarLabel")
        self.FileMenusLayout.addWidget(self.progressBarLabel, 3, 0, 1, 2)
        self.imgs_list_label = QtWidgets.QLabel(self.layoutWidget)
        self.imgs_list_label.setObjectName("imgs_list_label")
        self.FileMenusLayout.addWidget(self.imgs_list_label, 1, 1, 1, 1)
        self.mesfile_listw = QtWidgets.QListWidget(self.layoutWidget)
        self.mesfile_listw.setEnabled(False)
        self.mesfile_listw.setObjectName("mesfile_listw")
        self.FileMenusLayout.addWidget(self.mesfile_listw, 2, 0, 1, 1)
        self.listSplitSeq = QtWidgets.QListWidget(self.layoutWidget)
        self.listSplitSeq.setEnabled(False)
        self.listSplitSeq.setObjectName("listSplitSeq")
        self.FileMenusLayout.addWidget(self.listSplitSeq, 2, 2, 1, 1)
        self.imgs_list_label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.imgs_list_label_2.setObjectName("imgs_list_label_2")
        self.FileMenusLayout.addWidget(self.imgs_list_label_2, 1, 2, 1, 1)
        self.splitter = QtWidgets.QSplitter(self.splitter_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy)
        self.splitter.setMinimumSize(QtCore.QSize(0, 600))
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.layoutWidget1 = QtWidgets.QWidget(self.splitter)
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget1)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.add_roi_Btn = QtWidgets.QPushButton(self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.add_roi_Btn.sizePolicy().hasHeightForWidth())
        self.add_roi_Btn.setSizePolicy(sizePolicy)
        self.add_roi_Btn.setMinimumSize(QtCore.QSize(0, 10))
        self.add_roi_Btn.setMaximumSize(QtCore.QSize(100, 22))
        self.add_roi_Btn.setIconSize(QtCore.QSize(16, 16))
        self.add_roi_Btn.setObjectName("add_roi_Btn")
        self.gridLayout.addWidget(self.add_roi_Btn, 3, 1, 1, 1)
        self.btnSubArray = QtWidgets.QPushButton(self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.btnSubArray.sizePolicy().hasHeightForWidth())
        self.btnSubArray.setSizePolicy(sizePolicy)
        self.btnSubArray.setMinimumSize(QtCore.QSize(0, 10))
        self.btnSubArray.setMaximumSize(QtCore.QSize(100, 22))
        self.btnSubArray.setIconSize(QtCore.QSize(16, 16))
        self.btnSubArray.setCheckable(True)
        self.btnSubArray.setObjectName("btnSubArray")
        self.gridLayout.addWidget(self.btnSubArray, 2, 1, 1, 1)
        self.abortBtn = QtWidgets.QPushButton(self.layoutWidget1)
        self.abortBtn.setEnabled(False)
        self.abortBtn.setObjectName("abortBtn")
        self.gridLayout.addWidget(self.abortBtn, 0, 2, 1, 1)
        self.graphicsView = GraphicsView(self.layoutWidget1)
        self.graphicsView.setObjectName("graphicsView")
        self.gridLayout.addWidget(self.graphicsView, 1, 0, 6, 1)
        self.progressBar = QtWidgets.QProgressBar(self.layoutWidget1)
        self.progressBar.setEnabled(False)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout.addWidget(self.progressBar, 0, 0, 1, 2)
        self.btnChangeSMap = QtWidgets.QPushButton(self.layoutWidget1)
        self.btnChangeSMap.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.btnChangeSMap.sizePolicy().hasHeightForWidth())
        self.btnChangeSMap.setSizePolicy(sizePolicy)
        self.btnChangeSMap.setMinimumSize(QtCore.QSize(0, 10))
        self.btnChangeSMap.setMaximumSize(QtCore.QSize(100, 22))
        self.btnChangeSMap.setObjectName("btnChangeSMap")
        self.gridLayout.addWidget(self.btnChangeSMap, 2, 2, 1, 1)
        self.btnConcatSeqs = QtWidgets.QPushButton(self.layoutWidget1)
        self.btnConcatSeqs.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.btnConcatSeqs.sizePolicy().hasHeightForWidth())
        self.btnConcatSeqs.setSizePolicy(sizePolicy)
        self.btnConcatSeqs.setMinimumSize(QtCore.QSize(0, 10))
        self.btnConcatSeqs.setMaximumSize(QtCore.QSize(100, 22))
        self.btnConcatSeqs.setObjectName("btnConcatSeqs")
        self.gridLayout.addWidget(self.btnConcatSeqs, 5, 1, 1, 1)
        self.btnSplitSeq = QtWidgets.QPushButton(self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.btnSplitSeq.sizePolicy().hasHeightForWidth())
        self.btnSplitSeq.setSizePolicy(sizePolicy)
        self.btnSplitSeq.setMinimumSize(QtCore.QSize(0, 10))
        self.btnSplitSeq.setMaximumSize(QtCore.QSize(100, 22))
        self.btnSplitSeq.setObjectName("btnSplitSeq")
        self.gridLayout.addWidget(self.btnSplitSeq, 4, 1, 1, 1)
        self.resetscaleBtn = QtWidgets.QPushButton(self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.resetscaleBtn.sizePolicy().hasHeightForWidth())
        self.resetscaleBtn.setSizePolicy(sizePolicy)
        self.resetscaleBtn.setMinimumSize(QtCore.QSize(0, 10))
        self.resetscaleBtn.setMaximumSize(QtCore.QSize(100, 22))
        self.resetscaleBtn.setObjectName("resetscaleBtn")
        self.gridLayout.addWidget(self.resetscaleBtn, 6, 1, 1, 1)
        self.histogram = HistogramLUTWidget(self.layoutWidget1)
        self.histogram.setObjectName("histogram")
        self.gridLayout.addWidget(self.histogram, 1, 1, 1, 2)
        self.btnResetSMap = QtWidgets.QPushButton(self.layoutWidget1)
        self.btnResetSMap.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.btnResetSMap.sizePolicy().hasHeightForWidth())
        self.btnResetSMap.setSizePolicy(sizePolicy)
        self.btnResetSMap.setMinimumSize(QtCore.QSize(0, 10))
        self.btnResetSMap.setMaximumSize(QtCore.QSize(100, 22))
        self.btnResetSMap.setObjectName("btnResetSMap")
        self.gridLayout.addWidget(self.btnResetSMap, 3, 2, 1, 1)
        self.btnExport = QtWidgets.QPushButton(self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.btnExport.sizePolicy().hasHeightForWidth())
        self.btnExport.setSizePolicy(sizePolicy)
        self.btnExport.setMinimumSize(QtCore.QSize(0, 10))
        self.btnExport.setMaximumSize(QtCore.QSize(100, 22))
        self.btnExport.setObjectName("btnExport")
        self.gridLayout.addWidget(self.btnExport, 4, 2, 1, 1)
        self.btnAddCurrEnvToProj = QtWidgets.QPushButton(self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.btnAddCurrEnvToProj.sizePolicy().hasHeightForWidth())
        self.btnAddCurrEnvToProj.setSizePolicy(sizePolicy)
        self.btnAddCurrEnvToProj.setMinimumSize(QtCore.QSize(0, 10))
        self.btnAddCurrEnvToProj.setMaximumSize(QtCore.QSize(100, 22))
        self.btnAddCurrEnvToProj.setObjectName("btnAddCurrEnvToProj")
        self.gridLayout.addWidget(self.btnAddCurrEnvToProj, 5, 2, 1, 1)
        self.btnAddCurrEnvToProj_2 = QtWidgets.QPushButton(self.layoutWidget1)
        self.btnAddCurrEnvToProj_2.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.btnAddCurrEnvToProj_2.sizePolicy().hasHeightForWidth())
        self.btnAddCurrEnvToProj_2.setSizePolicy(sizePolicy)
        self.btnAddCurrEnvToProj_2.setMinimumSize(QtCore.QSize(0, 10))
        self.btnAddCurrEnvToProj_2.setMaximumSize(QtCore.QSize(100, 22))
        self.btnAddCurrEnvToProj_2.setObjectName("btnAddCurrEnvToProj_2")
        self.gridLayout.addWidget(self.btnAddCurrEnvToProj_2, 6, 2, 1, 1)
        self.roiPlot = PlotWidget(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.roiPlot.sizePolicy().hasHeightForWidth())
        self.roiPlot.setSizePolicy(sizePolicy)
        self.roiPlot.setMinimumSize(QtCore.QSize(0, 40))
        self.roiPlot.setObjectName("roiPlot")
        self.MotionCorGroup = QtWidgets.QGroupBox(self.splitter_2)
        self.MotionCorGroup.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.MotionCorGroup.sizePolicy().hasHeightForWidth())
        self.MotionCorGroup.setSizePolicy(sizePolicy)
        self.MotionCorGroup.setMinimumSize(QtCore.QSize(0, 150))
        self.MotionCorGroup.setObjectName("MotionCorGroup")
        self.layoutWidget2 = QtWidgets.QWidget(self.MotionCorGroup)
        self.layoutWidget2.setGeometry(QtCore.QRect(11, 30, 1101, 113))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lineEdAnimalID = QtWidgets.QLineEdit(self.layoutWidget2)
        self.lineEdAnimalID.setObjectName("lineEdAnimalID")
        self.horizontalLayout_2.addWidget(self.lineEdAnimalID)
        self.lineEdTrialID = QtWidgets.QLineEdit(self.layoutWidget2)
        self.lineEdTrialID.setObjectName("lineEdTrialID")
        self.horizontalLayout_2.addWidget(self.lineEdTrialID)
        self.btnSetID = QtWidgets.QPushButton(self.layoutWidget2)
        self.btnSetID.setObjectName("btnSetID")
        self.horizontalLayout_2.addWidget(self.btnSetID)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.rigMotCheckBox = QtWidgets.QCheckBox(self.layoutWidget2)
        self.rigMotCheckBox.setObjectName("rigMotCheckBox")
        self.verticalLayout_2.addWidget(self.rigMotCheckBox)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget2)
        self.pushButton.setCheckable(True)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.label_7 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_7.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout.addWidget(self.label_7)
        self.spinboxX = QtWidgets.QSpinBox(self.layoutWidget2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinboxX.sizePolicy().hasHeightForWidth())
        self.spinboxX.setSizePolicy(sizePolicy)
        self.spinboxX.setObjectName("spinboxX")
        self.horizontalLayout.addWidget(self.spinboxX)
        self.label_11 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_11.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout.addWidget(self.label_11)
        self.spinboxY = QtWidgets.QSpinBox(self.layoutWidget2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinboxY.sizePolicy().hasHeightForWidth())
        self.spinboxY.setSizePolicy(sizePolicy)
        self.spinboxY.setObjectName("spinboxY")
        self.horizontalLayout.addWidget(self.spinboxY)
        self.label_12 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_12.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout.addWidget(self.label_12)
        self.spinboxThreads = QtWidgets.QSpinBox(self.layoutWidget2)
        self.spinboxThreads.setMinimum(1)
        self.spinboxThreads.setObjectName("spinboxThreads")
        self.horizontalLayout.addWidget(self.spinboxThreads)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.spinboxIter = QtWidgets.QSpinBox(self.layoutWidget2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinboxIter.sizePolicy().hasHeightForWidth())
        self.spinboxIter.setSizePolicy(sizePolicy)
        self.spinboxIter.setObjectName("spinboxIter")
        self.horizontalLayout.addWidget(self.spinboxIter)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.btnAddToBatch = QtWidgets.QPushButton(self.layoutWidget2)
        self.btnAddToBatch.setObjectName("btnAddToBatch")
        self.horizontalLayout_4.addWidget(self.btnAddToBatch)
        self.btnMotCorrNow = QtWidgets.QPushButton(self.layoutWidget2)
        self.btnMotCorrNow.setObjectName("btnMotCorrNow")
        self.horizontalLayout_4.addWidget(self.btnMotCorrNow)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_7.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.elasMotCheckBox = QtWidgets.QCheckBox(self.layoutWidget2)
        self.elasMotCheckBox.setEnabled(False)
        self.elasMotCheckBox.setObjectName("elasMotCheckBox")
        self.verticalLayout.addWidget(self.elasMotCheckBox)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_4 = QtWidgets.QLabel(self.layoutWidget2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_6.addWidget(self.label_4)
        self.labelStridesValue = QtWidgets.QLabel(self.layoutWidget2)
        self.labelStridesValue.setText("")
        self.labelStridesValue.setObjectName("labelStridesValue")
        self.horizontalLayout_6.addWidget(self.labelStridesValue)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.sliderStrides = QtWidgets.QSlider(self.layoutWidget2)
        self.sliderStrides.setOrientation(QtCore.Qt.Horizontal)
        self.sliderStrides.setObjectName("sliderStrides")
        self.verticalLayout.addWidget(self.sliderStrides)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_5 = QtWidgets.QLabel(self.layoutWidget2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5)
        self.labelOverlapsValue = QtWidgets.QLabel(self.layoutWidget2)
        self.labelOverlapsValue.setText("")
        self.labelOverlapsValue.setObjectName("labelOverlapsValue")
        self.horizontalLayout_5.addWidget(self.labelOverlapsValue)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.sliderOverlaps = QtWidgets.QSlider(self.layoutWidget2)
        self.sliderOverlaps.setOrientation(QtCore.Qt.Horizontal)
        self.sliderOverlaps.setObjectName("sliderOverlaps")
        self.horizontalLayout_3.addWidget(self.sliderOverlaps)
        self.label_8 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_3.addWidget(self.label_8)
        self.spinboxUpsample = QtWidgets.QSpinBox(self.layoutWidget2)
        self.spinboxUpsample.setMinimum(1)
        self.spinboxUpsample.setObjectName("spinboxUpsample")
        self.horizontalLayout_3.addWidget(self.spinboxUpsample)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.spinboxMaxDev = QtWidgets.QSpinBox(self.layoutWidget2)
        self.spinboxMaxDev.setObjectName("spinboxMaxDev")
        self.horizontalLayout_3.addWidget(self.spinboxMaxDev)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_7.addLayout(self.verticalLayout)
        self.layoutWidget3 = QtWidgets.QWidget(self.splitter_3)
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.BatchesLayout = QtWidgets.QVBoxLayout(self.layoutWidget3)
        self.BatchesLayout.setContentsMargins(0, 0, 0, 0)
        self.BatchesLayout.setObjectName("BatchesLayout")
        self.batchLabel = QtWidgets.QLabel(self.layoutWidget3)
        self.batchLabel.setObjectName("batchLabel")
        self.BatchesLayout.addWidget(self.batchLabel)
        self.listwidgBatch = QtWidgets.QListWidget(self.layoutWidget3)
        self.listwidgBatch.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.listwidgBatch.setObjectName("listwidgBatch")
        self.BatchesLayout.addWidget(self.listwidgBatch)
        self.motioncorrlistLabel = QtWidgets.QLabel(self.layoutWidget3)
        self.motioncorrlistLabel.setObjectName("motioncorrlistLabel")
        self.BatchesLayout.addWidget(self.motioncorrlistLabel)
        self.listwidgMotCor = QtWidgets.QListWidget(self.layoutWidget3)
        self.listwidgMotCor.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.listwidgMotCor.setObjectName("listwidgMotCor")
        self.BatchesLayout.addWidget(self.listwidgMotCor)
        self.denoisedlistLabel = QtWidgets.QLabel(self.layoutWidget3)
        self.denoisedlistLabel.setObjectName("denoisedlistLabel")
        self.BatchesLayout.addWidget(self.denoisedlistLabel)
        self.listwidgDenoised = QtWidgets.QListWidget(self.layoutWidget3)
        self.listwidgDenoised.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.listwidgDenoised.setObjectName("listwidgDenoised")
        self.BatchesLayout.addWidget(self.listwidgDenoised)
        self.btnStartBatch = QtWidgets.QPushButton(self.layoutWidget3)
        self.btnStartBatch.setEnabled(False)
        self.btnStartBatch.setObjectName("btnStartBatch")
        self.BatchesLayout.addWidget(self.btnStartBatch)
        self.btnOpenBatch = QtWidgets.QPushButton(self.layoutWidget3)
        self.btnOpenBatch.setObjectName("btnOpenBatch")
        self.BatchesLayout.addWidget(self.btnOpenBatch)
        self.BtnAddSelProj = QtWidgets.QPushButton(self.layoutWidget3)
        self.BtnAddSelProj.setEnabled(False)
        self.BtnAddSelProj.setObjectName("BtnAddSelProj")
        self.BatchesLayout.addWidget(self.BtnAddSelProj)
        self.gridLayout_2.addWidget(self.splitter_3, 0, 0, 1, 1)
        self.splitter1 = QtWidgets.QSplitter(Form)
        self.splitter1.setGeometry(QtCore.QRect(0, 0, 0, 0))
        self.splitter1.setOrientation(QtCore.Qt.Vertical)
        self.splitter1.setObjectName("splitter1")
        self.splitter2 = QtWidgets.QSplitter(Form)
        self.splitter2.setGeometry(QtCore.QRect(0, 0, 0, 0))
        self.splitter2.setOrientation(QtCore.Qt.Vertical)
        self.splitter2.setObjectName("splitter2")

        self.retranslateUi(Form)
        self.rigMotCheckBox.toggled['bool'].connect(self.elasMotCheckBox.setEnabled)
        self.rigMotCheckBox.toggled['bool'].connect(self.btnAddToBatch.setEnabled)
        self.rigMotCheckBox.toggled['bool'].connect(self.btnMotCorrNow.setEnabled)
        self.sliderStrides.valueChanged['int'].connect(self.labelStridesValue.setNum)
        self.sliderOverlaps.valueChanged['int'].connect(self.labelOverlapsValue.setNum)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.openFileBtn.setText(_translate("Form", "Open file(s)"))
        self.mesfile_label.setText(_translate("Form", "MES file contents"))
        self.imgs_list_label.setText(_translate("Form", "Images/stacks"))
        self.imgs_list_label_2.setText(_translate("Form", "Splits of current sequence"))
        self.add_roi_Btn.setText(_translate("Form", "+ ROI"))
        self.btnSubArray.setText(_translate("Form", "Subarray"))
        self.abortBtn.setText(_translate("Form", "Abort"))
        self.btnChangeSMap.setToolTip(_translate("Form", "Set a Stimulus Map for only the image currently open"))
        self.btnChangeSMap.setText(_translate("Form", "Change sMap"))
        self.btnConcatSeqs.setText(_translate("Form", "Concat seqs"))
        self.btnSplitSeq.setText(_translate("Form", "Split seq"))
        self.resetscaleBtn.setText(_translate("Form", "Reset scale"))
        self.btnResetSMap.setToolTip(_translate("Form", "Reset the Stimulus Map to the one set for this mes file"))
        self.btnResetSMap.setText(_translate("Form", "Reset sMap"))
        self.btnExport.setText(_translate("Form", "Export view"))
        self.btnAddCurrEnvToProj.setText(_translate("Form", "Add to Project"))
        self.btnAddCurrEnvToProj_2.setText(_translate("Form", "Save changes"))
        self.MotionCorGroup.setTitle(_translate("Form", "Add to batch parameters"))
        self.lineEdAnimalID.setPlaceholderText(_translate("Form", "Animal ID"))
        self.lineEdTrialID.setPlaceholderText(_translate("Form", "Trial ID"))
        self.btnSetID.setText(_translate("Form", "Set"))
        self.rigMotCheckBox.setText(_translate("Form", "Rigid motion correction"))
        self.pushButton.setText(_translate("Form", "Measure"))
        self.label_7.setText(_translate("Form", " max shifts X: "))
        self.label_11.setText(_translate("Form", " max shifts Y: "))
        self.label_12.setText(_translate("Form", "threads: "))
        self.label_2.setText(_translate("Form", " iterations: "))
        self.btnAddToBatch.setText(_translate("Form", "Add to batch"))
        self.btnMotCorrNow.setText(_translate("Form", "Process now"))
        self.elasMotCheckBox.setText(_translate("Form", "Elastic motion correction"))
        self.label_4.setText(_translate("Form", "strides"))
        self.label_5.setText(_translate("Form", "overlaps"))
        self.label_8.setText(_translate("Form", " upsample:"))
        self.label_3.setText(_translate("Form", " max deviation:"))
        self.batchLabel.setText(_translate("Form", "Batch"))
        self.motioncorrlistLabel.setText(_translate("Form", "Motion Corrected"))
        self.denoisedlistLabel.setText(_translate("Form", "Denoised"))
        self.btnStartBatch.setText(_translate("Form", "Start Batch"))
        self.btnOpenBatch.setText(_translate("Form", "Open Batch"))
        self.BtnAddSelProj.setText(_translate("Form", "Add selection to project"))

from ..widgets.GraphicsView import GraphicsView
from ..widgets.HistogramLUTWidget import HistogramLUTWidget
from ..widgets.PlotWidget import PlotWidget
