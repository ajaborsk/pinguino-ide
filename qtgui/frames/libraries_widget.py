# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/yeison/.virtualenvs/pinguino_env/pinguino/pinguino-ide/qtgui/frames/libraries_widget.ui'
#
# Created: Wed Jan  8 21:17:47 2014
#      by: pyside-uic 0.2.14 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_LibraryManager(object):
    def setupUi(self, LibraryManager):
        LibraryManager.setObjectName("LibraryManager")
        LibraryManager.resize(839, 368)
        self.centralwidget = QtGui.QWidget(LibraryManager)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_close = QtGui.QPushButton(self.centralwidget)
        self.pushButton_close.setObjectName("pushButton_close")
        self.gridLayout.addWidget(self.pushButton_close, 1, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtGui.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_2 = QtGui.QGridLayout(self.tab)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tableWidget_libs = QtGui.QTableWidget(self.tab)
        self.tableWidget_libs.setAlternatingRowColors(True)
        self.tableWidget_libs.setVerticalScrollMode(QtGui.QAbstractItemView.ScrollPerPixel)
        self.tableWidget_libs.setHorizontalScrollMode(QtGui.QAbstractItemView.ScrollPerPixel)
        self.tableWidget_libs.setGridStyle(QtCore.Qt.DotLine)
        self.tableWidget_libs.setWordWrap(False)
        self.tableWidget_libs.setCornerButtonEnabled(False)
        self.tableWidget_libs.setObjectName("tableWidget_libs")
        self.tableWidget_libs.setColumnCount(4)
        self.tableWidget_libs.setRowCount(6)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_libs.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_libs.setVerticalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_libs.setVerticalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_libs.setVerticalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_libs.setVerticalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_libs.setVerticalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_libs.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_libs.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_libs.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_libs.setHorizontalHeaderItem(3, item)
        self.tableWidget_libs.horizontalHeader().setHighlightSections(False)
        self.tableWidget_libs.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_libs.verticalHeader().setVisible(False)
        self.gridLayout_2.addWidget(self.tableWidget_libs, 0, 0, 1, 1)
        self.pushButton_apply = QtGui.QPushButton(self.tab)
        self.pushButton_apply.setEnabled(False)
        self.pushButton_apply.setMinimumSize(QtCore.QSize(241, 0))
        self.pushButton_apply.setMaximumSize(QtCore.QSize(241, 16777215))
        self.pushButton_apply.setObjectName("pushButton_apply")
        self.gridLayout_2.addWidget(self.pushButton_apply, 1, 0, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_3 = QtGui.QGridLayout(self.tab_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.tableWidget_sources = QtGui.QTableWidget(self.tab_2)
        self.tableWidget_sources.setAutoFillBackground(True)
        self.tableWidget_sources.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget_sources.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget_sources.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tableWidget_sources.setAlternatingRowColors(True)
        self.tableWidget_sources.setVerticalScrollMode(QtGui.QAbstractItemView.ScrollPerPixel)
        self.tableWidget_sources.setHorizontalScrollMode(QtGui.QAbstractItemView.ScrollPerPixel)
        self.tableWidget_sources.setGridStyle(QtCore.Qt.DotLine)
        self.tableWidget_sources.setObjectName("tableWidget_sources")
        self.tableWidget_sources.setColumnCount(2)
        self.tableWidget_sources.setRowCount(6)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_sources.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_sources.setVerticalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_sources.setVerticalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_sources.setVerticalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_sources.setVerticalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_sources.setVerticalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_sources.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_sources.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.tableWidget_sources.setItem(1, 0, item)
        self.tableWidget_sources.horizontalHeader().setHighlightSections(False)
        self.tableWidget_sources.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_sources.verticalHeader().setVisible(False)
        self.tableWidget_sources.verticalHeader().setHighlightSections(True)
        self.tableWidget_sources.verticalHeader().setStretchLastSection(False)
        self.gridLayout_3.addWidget(self.tableWidget_sources, 1, 0, 1, 2)
        self.pushButton_add = QtGui.QPushButton(self.tab_2)
        self.pushButton_add.setObjectName("pushButton_add")
        self.gridLayout_3.addWidget(self.pushButton_add, 0, 1, 1, 1)
        self.pushButton_update = QtGui.QPushButton(self.tab_2)
        self.pushButton_update.setEnabled(False)
        self.pushButton_update.setMinimumSize(QtCore.QSize(241, 0))
        self.pushButton_update.setMaximumSize(QtCore.QSize(241, 16777215))
        self.pushButton_update.setObjectName("pushButton_update")
        self.gridLayout_3.addWidget(self.pushButton_update, 2, 0, 1, 1)
        self.lineEdit_source = QtGui.QLineEdit(self.tab_2)
        self.lineEdit_source.setObjectName("lineEdit_source")
        self.gridLayout_3.addWidget(self.lineEdit_source, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 3)
        LibraryManager.setCentralWidget(self.centralwidget)

        self.retranslateUi(LibraryManager)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(LibraryManager)

    def retranslateUi(self, LibraryManager):
        LibraryManager.setWindowTitle(QtGui.QApplication.translate("LibraryManager", "LibraryManager", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_close.setText(QtGui.QApplication.translate("LibraryManager", "Close", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget_libs.verticalHeaderItem(0).setText(QtGui.QApplication.translate("LibraryManager", "New Row", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget_libs.verticalHeaderItem(1).setText(QtGui.QApplication.translate("LibraryManager", "New Row", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget_libs.verticalHeaderItem(2).setText(QtGui.QApplication.translate("LibraryManager", "New Row", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget_libs.verticalHeaderItem(3).setText(QtGui.QApplication.translate("LibraryManager", "New Row", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget_libs.verticalHeaderItem(4).setText(QtGui.QApplication.translate("LibraryManager", "New Row", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget_libs.verticalHeaderItem(5).setText(QtGui.QApplication.translate("LibraryManager", "New Row", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget_libs.horizontalHeaderItem(0).setText(QtGui.QApplication.translate("LibraryManager", "Library", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget_libs.horizontalHeaderItem(1).setText(QtGui.QApplication.translate("LibraryManager", "Architecture", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget_libs.horizontalHeaderItem(2).setText(QtGui.QApplication.translate("LibraryManager", "Author", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget_libs.horizontalHeaderItem(3).setText(QtGui.QApplication.translate("LibraryManager", "Description", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_apply.setText(QtGui.QApplication.translate("LibraryManager", "Apply", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtGui.QApplication.translate("LibraryManager", "Installed", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget_sources.verticalHeaderItem(0).setText(QtGui.QApplication.translate("LibraryManager", "New Row", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget_sources.verticalHeaderItem(1).setText(QtGui.QApplication.translate("LibraryManager", "New Row", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget_sources.verticalHeaderItem(2).setText(QtGui.QApplication.translate("LibraryManager", "New Row", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget_sources.verticalHeaderItem(3).setText(QtGui.QApplication.translate("LibraryManager", "New Row", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget_sources.verticalHeaderItem(4).setText(QtGui.QApplication.translate("LibraryManager", "New Row", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget_sources.verticalHeaderItem(5).setText(QtGui.QApplication.translate("LibraryManager", "New Row", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget_sources.horizontalHeaderItem(0).setText(QtGui.QApplication.translate("LibraryManager", "Name", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget_sources.horizontalHeaderItem(1).setText(QtGui.QApplication.translate("LibraryManager", "Repository", None, QtGui.QApplication.UnicodeUTF8))
        __sortingEnabled = self.tableWidget_sources.isSortingEnabled()
        self.tableWidget_sources.setSortingEnabled(False)
        self.tableWidget_sources.setSortingEnabled(__sortingEnabled)
        self.pushButton_add.setText(QtGui.QApplication.translate("LibraryManager", "Add", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_update.setText(QtGui.QApplication.translate("LibraryManager", "Update or Install selected", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QtGui.QApplication.translate("LibraryManager", "Sources", None, QtGui.QApplication.UnicodeUTF8))

