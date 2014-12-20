# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'R2DB.ui'
#
# Created: Tue Oct 14 09:12:57 2014
#      by: PyQt4 UI code generator 4.11
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(514, 264)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.order_rename = QtGui.QPushButton(self.centralwidget)
        self.order_rename.setGeometry(QtCore.QRect(210, 10, 75, 23))
        self.order_rename.setObjectName(_fromUtf8("order_rename"))
        self.pathname = QtGui.QLineEdit(self.centralwidget)
        self.pathname.setGeometry(QtCore.QRect(70, 10, 131, 20))
        self.pathname.setObjectName(_fromUtf8("pathname"))
        self.widename = QtGui.QLineEdit(self.centralwidget)
        self.widename.setGeometry(QtCore.QRect(370, 10, 51, 20))
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.widename.setFont(font)
        self.widename.setObjectName(_fromUtf8("widename"))
        self.order_rename_2 = QtGui.QPushButton(self.centralwidget)
        self.order_rename_2.setGeometry(QtCore.QRect(430, 10, 75, 23))
        self.order_rename_2.setObjectName(_fromUtf8("order_rename_2"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(310, 10, 51, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 51, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.srcreplace = QtGui.QPushButton(self.centralwidget)
        self.srcreplace.setGeometry(QtCore.QRect(70, 50, 75, 23))
        self.srcreplace.setObjectName(_fromUtf8("srcreplace"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 514, 17))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.order_rename.setText(_translate("MainWindow", "文件乱序", None))
        self.order_rename_2.setText(_translate("MainWindow", "标题重排", None))
        self.label.setText(_translate("MainWindow", "字符宽度", None))
        self.label_2.setText(_translate("MainWindow", "文件路径", None))
        self.srcreplace.setText(_translate("MainWindow", "src替换", None))

