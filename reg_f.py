import sys
from PyQt5 import QtWidgets, QtCore, uic
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class MainWWindow( QtWidgets.QMainWindow ):
    def __init__(self, parent = None):
        super(MainWWindow, self).__init__(parent)
        self.ui = uic.loadUi("reg_w.ui")
        self.form()
        self.ui.show()
    def openFile(self):
        self.fileD = QFileDialog.getOpenFileName(self,"Open file",'/', "*.jpg *.png")
    def form(self):
        self.ui.pushButton_3.clicked.connect(self.openFile)





if __name__ == '__main__':
    app = QtWidgets.QApplication ( sys.argv )
    window = MainWWindow()
    sys.exit ( app.exec () )