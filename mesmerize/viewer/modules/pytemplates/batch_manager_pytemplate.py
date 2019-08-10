# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './ui_files/batch_manager_pytemplate.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1052, 801)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.labelBatchPath = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelBatchPath.sizePolicy().hasHeightForWidth())
        self.labelBatchPath.setSizePolicy(sizePolicy)
        self.labelBatchPath.setMinimumSize(QtCore.QSize(0, 30))
        self.labelBatchPath.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.labelBatchPath.setFont(font)
        self.labelBatchPath.setText("")
        self.labelBatchPath.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.labelBatchPath.setObjectName("labelBatchPath")
        self.verticalLayout_5.addWidget(self.labelBatchPath)
        self.splitter_3 = QtWidgets.QSplitter(Form)
        self.splitter_3.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_3.setObjectName("splitter_3")
        self.splitter = QtWidgets.QSplitter(self.splitter_3)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.widget = QtWidgets.QWidget(self.splitter)
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.listWidgetItemNumbers = QtWidgets.QListWidget(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidgetItemNumbers.sizePolicy().hasHeightForWidth())
        self.listWidgetItemNumbers.setSizePolicy(sizePolicy)
        self.listWidgetItemNumbers.setMinimumSize(QtCore.QSize(30, 0))
        self.listWidgetItemNumbers.setObjectName("listWidgetItemNumbers")
        self.horizontalLayout.addWidget(self.listWidgetItemNumbers)
        self.listwBatch = QtWidgets.QListWidget(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(10)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listwBatch.sizePolicy().hasHeightForWidth())
        self.listwBatch.setSizePolicy(sizePolicy)
        self.listwBatch.setObjectName("listwBatch")
        self.horizontalLayout.addWidget(self.listwBatch)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.lineEditFindItem = QtWidgets.QLineEdit(self.widget)
        self.lineEditFindItem.setObjectName("lineEditFindItem")
        self.horizontalLayout_2.addWidget(self.lineEditFindItem)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.btnStart = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnStart.sizePolicy().hasHeightForWidth())
        self.btnStart.setSizePolicy(sizePolicy)
        self.btnStart.setMinimumSize(QtCore.QSize(55, 0))
        self.btnStart.setMaximumSize(QtCore.QSize(16777215, 50))
        self.btnStart.setBaseSize(QtCore.QSize(60, 0))
        self.btnStart.setObjectName("btnStart")
        self.gridLayout.addWidget(self.btnStart, 0, 0, 1, 1)
        self.btnStartAtSelection = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnStartAtSelection.sizePolicy().hasHeightForWidth())
        self.btnStartAtSelection.setSizePolicy(sizePolicy)
        self.btnStartAtSelection.setMinimumSize(QtCore.QSize(125, 0))
        self.btnStartAtSelection.setMaximumSize(QtCore.QSize(16777215, 50))
        self.btnStartAtSelection.setBaseSize(QtCore.QSize(60, 0))
        self.btnStartAtSelection.setObjectName("btnStartAtSelection")
        self.gridLayout.addWidget(self.btnStartAtSelection, 0, 1, 1, 2)
        self.btnDelete = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnDelete.sizePolicy().hasHeightForWidth())
        self.btnDelete.setSizePolicy(sizePolicy)
        self.btnDelete.setMinimumSize(QtCore.QSize(110, 0))
        self.btnDelete.setMaximumSize(QtCore.QSize(16777215, 50))
        self.btnDelete.setObjectName("btnDelete")
        self.gridLayout.addWidget(self.btnDelete, 0, 3, 1, 2)
        self.btnExportShScripts = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnExportShScripts.sizePolicy().hasHeightForWidth())
        self.btnExportShScripts.setSizePolicy(sizePolicy)
        self.btnExportShScripts.setMaximumSize(QtCore.QSize(16777215, 50))
        self.btnExportShScripts.setObjectName("btnExportShScripts")
        self.gridLayout.addWidget(self.btnExportShScripts, 0, 5, 1, 1)
        self.btnAbort = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnAbort.sizePolicy().hasHeightForWidth())
        self.btnAbort.setSizePolicy(sizePolicy)
        self.btnAbort.setMinimumSize(QtCore.QSize(55, 0))
        self.btnAbort.setMaximumSize(QtCore.QSize(16777215, 50))
        self.btnAbort.setBaseSize(QtCore.QSize(60, 0))
        self.btnAbort.setObjectName("btnAbort")
        self.gridLayout.addWidget(self.btnAbort, 1, 0, 1, 1)
        self.btnNew = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnNew.sizePolicy().hasHeightForWidth())
        self.btnNew.setSizePolicy(sizePolicy)
        self.btnNew.setMinimumSize(QtCore.QSize(80, 0))
        self.btnNew.setMaximumSize(QtCore.QSize(16777215, 50))
        self.btnNew.setBaseSize(QtCore.QSize(60, 0))
        self.btnNew.setObjectName("btnNew")
        self.gridLayout.addWidget(self.btnNew, 1, 1, 1, 1)
        self.btnOpen = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnOpen.sizePolicy().hasHeightForWidth())
        self.btnOpen.setSizePolicy(sizePolicy)
        self.btnOpen.setMinimumSize(QtCore.QSize(80, 0))
        self.btnOpen.setMaximumSize(QtCore.QSize(16777215, 50))
        self.btnOpen.setBaseSize(QtCore.QSize(60, 0))
        self.btnOpen.setObjectName("btnOpen")
        self.gridLayout.addWidget(self.btnOpen, 1, 2, 1, 2)
        self.btnViewInput = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnViewInput.sizePolicy().hasHeightForWidth())
        self.btnViewInput.setSizePolicy(sizePolicy)
        self.btnViewInput.setMinimumSize(QtCore.QSize(75, 0))
        self.btnViewInput.setMaximumSize(QtCore.QSize(16777215, 50))
        self.btnViewInput.setBaseSize(QtCore.QSize(70, 0))
        self.btnViewInput.setObjectName("btnViewInput")
        self.gridLayout.addWidget(self.btnViewInput, 1, 4, 1, 1)
        self.btnCompress = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnCompress.sizePolicy().hasHeightForWidth())
        self.btnCompress.setSizePolicy(sizePolicy)
        self.btnCompress.setMaximumSize(QtCore.QSize(16777215, 50))
        self.btnCompress.setObjectName("btnCompress")
        self.gridLayout.addWidget(self.btnCompress, 1, 5, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.checkBoxUseWorkDir = QtWidgets.QCheckBox(self.widget)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.checkBoxUseWorkDir.setFont(font)
        self.checkBoxUseWorkDir.setObjectName("checkBoxUseWorkDir")
        self.verticalLayout.addWidget(self.checkBoxUseWorkDir)
        self.progressBar = QtWidgets.QProgressBar(self.widget)
        self.progressBar.setMinimum(0)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(True)
        self.progressBar.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout.addWidget(self.progressBar)
        self.scrollArea = QtWidgets.QScrollArea(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 700, 327))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.textBrowserItemInfo = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents)
        self.textBrowserItemInfo.setObjectName("textBrowserItemInfo")
        self.verticalLayout_2.addWidget(self.textBrowserItemInfo)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.splitter_2 = QtWidgets.QSplitter(self.splitter_3)
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName("splitter_2")
        self.scrollAreaStdOut = QtWidgets.QScrollArea(self.splitter_2)
        self.scrollAreaStdOut.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.scrollAreaStdOut.sizePolicy().hasHeightForWidth())
        self.scrollAreaStdOut.setSizePolicy(sizePolicy)
        self.scrollAreaStdOut.setWidgetResizable(True)
        self.scrollAreaStdOut.setObjectName("scrollAreaStdOut")
        self.scrollAreaWidgetContents_4 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_4.setGeometry(QtCore.QRect(0, 0, 331, 367))
        self.scrollAreaWidgetContents_4.setObjectName("scrollAreaWidgetContents_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_4)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.textBrowserStdOut = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents_4)
        self.textBrowserStdOut.setObjectName("textBrowserStdOut")
        self.verticalLayout_4.addWidget(self.textBrowserStdOut)
        self.scrollAreaStdOut.setWidget(self.scrollAreaWidgetContents_4)
        self.scrollAreaOutputInfo = QtWidgets.QScrollArea(self.splitter_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.scrollAreaOutputInfo.sizePolicy().hasHeightForWidth())
        self.scrollAreaOutputInfo.setSizePolicy(sizePolicy)
        self.scrollAreaOutputInfo.setWidgetResizable(True)
        self.scrollAreaOutputInfo.setObjectName("scrollAreaOutputInfo")
        self.scrollAreaWidgetContents_6 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_6.setGeometry(QtCore.QRect(0, 0, 331, 367))
        self.scrollAreaWidgetContents_6.setObjectName("scrollAreaWidgetContents_6")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_6)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.textBrowserOutputInfo = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents_6)
        self.textBrowserOutputInfo.setObjectName("textBrowserOutputInfo")
        self.verticalLayout_3.addWidget(self.textBrowserOutputInfo)
        self.scrollAreaOutputInfo.setWidget(self.scrollAreaWidgetContents_6)
        self.verticalLayout_5.addWidget(self.splitter_3)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.listwBatch, self.btnStart)
        Form.setTabOrder(self.btnStart, self.btnStartAtSelection)
        Form.setTabOrder(self.btnStartAtSelection, self.btnDelete)
        Form.setTabOrder(self.btnDelete, self.btnAbort)
        Form.setTabOrder(self.btnAbort, self.btnNew)
        Form.setTabOrder(self.btnNew, self.btnOpen)
        Form.setTabOrder(self.btnOpen, self.btnViewInput)
        Form.setTabOrder(self.btnViewInput, self.scrollArea)
        Form.setTabOrder(self.scrollArea, self.textBrowserItemInfo)
        Form.setTabOrder(self.textBrowserItemInfo, self.textBrowserStdOut)
        Form.setTabOrder(self.textBrowserStdOut, self.scrollAreaStdOut)
        Form.setTabOrder(self.scrollAreaStdOut, self.textBrowserOutputInfo)
        Form.setTabOrder(self.textBrowserOutputInfo, self.scrollAreaOutputInfo)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Find:"))
        self.btnStart.setText(_translate("Form", "Start"))
        self.btnStartAtSelection.setText(_translate("Form", "Start at selection"))
        self.btnDelete.setText(_translate("Form", "Delete selection"))
        self.btnExportShScripts.setText(_translate("Form", "Export shell scripts"))
        self.btnAbort.setText(_translate("Form", "Abort"))
        self.btnNew.setText(_translate("Form", "New Batch"))
        self.btnOpen.setText(_translate("Form", "Open Batch"))
        self.btnViewInput.setText(_translate("Form", "View Input"))
        self.btnCompress.setText(_translate("Form", "Compress"))
        self.checkBoxUseWorkDir.setToolTip(_translate("Form", "Use a temporary working directory to process each batch item. Moves output back to batch directory when done. Useful if you have a very fast filesystem with limited capacity."))
        self.checkBoxUseWorkDir.setText(_translate("Form", "Use work dir"))
        self.textBrowserItemInfo.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Noto Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Sans Serif\'; font-size:9pt;\"><br /></p></body></html>"))

