# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created: Wed Oct 16 19:31:24 2013
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName(_fromUtf8("mainWindow"))
        mainWindow.resize(1067, 714)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/hl2mt.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        mainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(mainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.processButton = QtGui.QPushButton(self.centralwidget)
        self.processButton.setIconSize(QtCore.QSize(32, 32))
        self.processButton.setObjectName(_fromUtf8("processButton"))
        self.gridLayout.addWidget(self.processButton, 1, 0, 1, 1)
        self.createButton = QtGui.QPushButton(self.centralwidget)
        self.createButton.setIconSize(QtCore.QSize(32, 32))
        self.createButton.setObjectName(_fromUtf8("createButton"))
        self.gridLayout.addWidget(self.createButton, 1, 1, 1, 1)
        self.tableWidget = QtGui.QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.gridLayout.addWidget(self.tableWidget, 0, 0, 1, 2)
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1067, 29))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuConfig = QtGui.QMenu(self.menubar)
        self.menuConfig.setObjectName(_fromUtf8("menuConfig"))
        self.menuOptions = QtGui.QMenu(self.menubar)
        self.menuOptions.setObjectName(_fromUtf8("menuOptions"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(mainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        mainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(mainWindow)
        self.toolBar.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        mainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionProperties = QtGui.QAction(mainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/user.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionProperties.setIcon(icon1)
        self.actionProperties.setIconVisibleInMenu(True)
        self.actionProperties.setObjectName(_fromUtf8("actionProperties"))
        self.actionOutput = QtGui.QAction(mainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/pencil.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOutput.setIcon(icon2)
        self.actionOutput.setIconVisibleInMenu(True)
        self.actionOutput.setObjectName(_fromUtf8("actionOutput"))
        self.actionColors = QtGui.QAction(mainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/colors.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionColors.setIcon(icon3)
        self.actionColors.setIconVisibleInMenu(True)
        self.actionColors.setObjectName(_fromUtf8("actionColors"))
        self.actionIndexing = QtGui.QAction(mainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/database_add.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionIndexing.setIcon(icon4)
        self.actionIndexing.setIconVisibleInMenu(True)
        self.actionIndexing.setObjectName(_fromUtf8("actionIndexing"))
        self.actionImport = QtGui.QAction(mainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/import.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionImport.setIcon(icon5)
        self.actionImport.setIconVisibleInMenu(True)
        self.actionImport.setObjectName(_fromUtf8("actionImport"))
        self.actionSave = QtGui.QAction(mainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/export.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave.setIcon(icon6)
        self.actionSave.setIconVisibleInMenu(True)
        self.actionSave.setObjectName(_fromUtf8("actionSave"))
        self.actionFolders = QtGui.QAction(mainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/folder.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionFolders.setIcon(icon7)
        self.actionFolders.setIconVisibleInMenu(True)
        self.actionFolders.setObjectName(_fromUtf8("actionFolders"))
        self.actionAbout = QtGui.QAction(mainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/info.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAbout.setIcon(icon8)
        self.actionAbout.setIconVisibleInMenu(True)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.actionExit = QtGui.QAction(mainWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionHelp = QtGui.QAction(mainWindow)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/help_book.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionHelp.setIcon(icon9)
        self.actionHelp.setIconVisibleInMenu(True)
        self.actionHelp.setObjectName(_fromUtf8("actionHelp"))
        self.menuConfig.addAction(self.actionImport)
        self.menuConfig.addAction(self.actionSave)
        self.menuConfig.addSeparator()
        self.menuConfig.addAction(self.actionExit)
        self.menuOptions.addAction(self.actionFolders)
        self.menuOptions.addAction(self.actionProperties)
        self.menuOptions.addAction(self.actionColors)
        self.menuOptions.addAction(self.actionIndexing)
        self.menuOptions.addAction(self.actionOutput)
        self.menuHelp.addAction(self.actionHelp)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuConfig.menuAction())
        self.menubar.addAction(self.menuOptions.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.toolBar.addAction(self.actionImport)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionFolders)
        self.toolBar.addAction(self.actionProperties)
        self.toolBar.addAction(self.actionColors)
        self.toolBar.addAction(self.actionIndexing)
        self.toolBar.addAction(self.actionOutput)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionHelp)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(QtGui.QApplication.translate("mainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.processButton.setText(QtGui.QApplication.translate("mainWindow", "Process Files", None, QtGui.QApplication.UnicodeUTF8))
        self.createButton.setText(QtGui.QApplication.translate("mainWindow", "Create Tokens", None, QtGui.QApplication.UnicodeUTF8))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(QtGui.QApplication.translate("mainWindow", "Filename", None, QtGui.QApplication.UnicodeUTF8))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(QtGui.QApplication.translate("mainWindow", "Source", None, QtGui.QApplication.UnicodeUTF8))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(QtGui.QApplication.translate("mainWindow", "Name", None, QtGui.QApplication.UnicodeUTF8))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(QtGui.QApplication.translate("mainWindow", "Portrait", None, QtGui.QApplication.UnicodeUTF8))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(QtGui.QApplication.translate("mainWindow", "Token Image", None, QtGui.QApplication.UnicodeUTF8))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(QtGui.QApplication.translate("mainWindow", "Destination", None, QtGui.QApplication.UnicodeUTF8))
        self.menuConfig.setTitle(QtGui.QApplication.translate("mainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuOptions.setTitle(QtGui.QApplication.translate("mainWindow", "Options", None, QtGui.QApplication.UnicodeUTF8))
        self.menuHelp.setTitle(QtGui.QApplication.translate("mainWindow", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar.setWindowTitle(QtGui.QApplication.translate("mainWindow", "toolBar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionProperties.setText(QtGui.QApplication.translate("mainWindow", "Token Properties", None, QtGui.QApplication.UnicodeUTF8))
        self.actionProperties.setShortcut(QtGui.QApplication.translate("mainWindow", "Ctrl+P", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOutput.setText(QtGui.QApplication.translate("mainWindow", "Output Options", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOutput.setToolTip(QtGui.QApplication.translate("mainWindow", "Token Output Options", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOutput.setShortcut(QtGui.QApplication.translate("mainWindow", "Ctrl+O", None, QtGui.QApplication.UnicodeUTF8))
        self.actionColors.setText(QtGui.QApplication.translate("mainWindow", "Macro Colors", None, QtGui.QApplication.UnicodeUTF8))
        self.actionColors.setToolTip(QtGui.QApplication.translate("mainWindow", "Token Macro Colors", None, QtGui.QApplication.UnicodeUTF8))
        self.actionColors.setShortcut(QtGui.QApplication.translate("mainWindow", "Ctrl+C", None, QtGui.QApplication.UnicodeUTF8))
        self.actionIndexing.setText(QtGui.QApplication.translate("mainWindow", "Indexing Options", None, QtGui.QApplication.UnicodeUTF8))
        self.actionIndexing.setToolTip(QtGui.QApplication.translate("mainWindow", "Token Indexing Options", None, QtGui.QApplication.UnicodeUTF8))
        self.actionIndexing.setShortcut(QtGui.QApplication.translate("mainWindow", "Ctrl+I", None, QtGui.QApplication.UnicodeUTF8))
        self.actionImport.setText(QtGui.QApplication.translate("mainWindow", "Import Config", None, QtGui.QApplication.UnicodeUTF8))
        self.actionImport.setToolTip(QtGui.QApplication.translate("mainWindow", "Import Config", None, QtGui.QApplication.UnicodeUTF8))
        self.actionImport.setShortcut(QtGui.QApplication.translate("mainWindow", "Ctrl+F", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave.setText(QtGui.QApplication.translate("mainWindow", "Save Config As...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave.setShortcut(QtGui.QApplication.translate("mainWindow", "Ctrl+S", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFolders.setText(QtGui.QApplication.translate("mainWindow", "Token Folders", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFolders.setToolTip(QtGui.QApplication.translate("mainWindow", "Select Token Folders", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFolders.setShortcut(QtGui.QApplication.translate("mainWindow", "Ctrl+T", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout.setText(QtGui.QApplication.translate("mainWindow", "About", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout.setToolTip(QtGui.QApplication.translate("mainWindow", "About hl2mt", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExit.setText(QtGui.QApplication.translate("mainWindow", "Exit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExit.setShortcut(QtGui.QApplication.translate("mainWindow", "Ctrl+X", None, QtGui.QApplication.UnicodeUTF8))
        self.actionHelp.setText(QtGui.QApplication.translate("mainWindow", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.actionHelp.setShortcut(QtGui.QApplication.translate("mainWindow", "Ctrl+H", None, QtGui.QApplication.UnicodeUTF8))

import icons_rc
