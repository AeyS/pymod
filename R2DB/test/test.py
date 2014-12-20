#coding:utf-8

def addprojectpath():
    '''添加项目到系统路径'''
    import os
    import sys
    sys.path.append('../')


addprojectpath()
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from taobao import run
import sys
import main

class test_ui(QMainWindow, main.Ui_MainWindow):
    """docstring for test_ui"""
    def __init__(self, parent=None):
        super(test_ui, self).__init__(parent)
        self.setupUi(self)
        self.pathname.setText('E:/20140905taobao/upload')
        self.widename.setText('60')
        QObject.connect(self.order_rename_2, SIGNAL("clicked()"),self.sort)
        QObject.connect(self.order_rename, SIGNAL("clicked()"),self.pic_rename)
        QObject.connect(self.srcreplace, SIGNAL("clicked()"),self.picCan)

    def sort(self):
        run.sort(int(unicode(QString(self.widename.text()))))

    def pic_rename(self):
        run.pic_rename(unicode(QString(self.pathname.text())))

    def picCan(self):
        run.picCan()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = test_ui()
    dialog.show()
    sys.exit(app.exec_())
