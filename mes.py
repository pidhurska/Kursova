import sys
from PyQt5 import QtWidgets, QtCore, uic
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap

class Warning_drl( QtWidgets.QMainWindow ):
    def __init__(self, parent = None):
        super(Warning_drl, self).__init__(parent)
        self.xapp = QApplication ( sys.argv )
        self.msg = QMessageBox ()
        self.msg.setIcon ( QMessageBox.Warning )
        self.msg.setWindowTitle ( "Warning" )
        self.msg.setText ( "Login or password isn`t right", )



    def show_prof(self):
        self.msg.show()



class Warning_d( QtWidgets.QMainWindow ):
    def __init__(self, parent = None):
        super(Warning_d, self).__init__(parent)
        self.app = QApplication ( sys.argv )
        self.msg = QMessageBox ()
        self.msg.setIcon ( QMessageBox.Warning )
        self.msg.setWindowTitle ( "Warning" )
        self.msg.setText ( "You did not fill right entry fields \n Your string must content min 6 characters", )



    def show_prof(self):
        self.msg.show()


class Warning_a( QtWidgets.QMainWindow ):
    def __init__(self, parent = None):
        super(Warning_a, self).__init__(parent)
        self.app = QApplication ( sys.argv )
        self.msg = QMessageBox ()
        self.msg.setIcon ( QMessageBox.Warning )
        self.msg.setWindowTitle ( "Warning" )
        self.msg.setText ( "Your login is already used", )



    def show_prof(self):
        self.msg.show()


class Addinfo( QtWidgets.QMainWindow ):
    def __init__(self, parent = None):
        super(Addinfo, self).__init__(parent)

        self.ui_add = uic.loadUi( "add_info_w.ui" )
        self.text1=self.ui_add.lineEdit
        self.test_event = 0

        self.button_ok = self.ui_add.pushButton
        self.button_ok.clicked.connect ( self.on_click )

    def on_click(self):
        self.text = self.text1.text ()
        f = open ( 'logdata.txt', 'w' )
        f.write ( self.text)
        f.close ()
        self.ui_add.hide()


    def show_prof(self):
        self.ui_add.show ()




