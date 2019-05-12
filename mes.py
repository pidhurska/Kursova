import sys
from PyQt5 import QtWidgets, QtCore, uic
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import *

#import
from PyQt5.QtWidgets import *

class Warning_drl( QtWidgets.QMainWindow ):
    def __init__(self, parent = None):
        super(Warning_drl, self).__init__(parent)
        #Set interface
        self.xapp = QApplication ( sys.argv )
        #type
        self.msg = QMessageBox ()
        self.msg.setIcon ( QMessageBox.Warning )
        #Set title
        self.msg.setWindowTitle ( "Warning" )
        #Set message
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
        self.msg.setText ( "You did not fill right entry fields \n Your string must content min 4 characters", )



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


class Warning_city( QtWidgets.QMainWindow ):
    def __init__(self, parent = None):
        super(Warning_city, self).__init__(parent)
        self.app = QApplication ( sys.argv )
        self.msg = QMessageBox ()
        self.msg.setIcon ( QMessageBox.Warning )
        self.msg.setWindowTitle ( "Warning" )
        self.msg.setText ( "Your choose same city", )



    def show_prof(self):
        self.msg.show()

class Warning_data( QtWidgets.QMainWindow ):
    def __init__(self, parent = None):
        super(Warning_data, self).__init__(parent)
        self.app = QApplication ( sys.argv )
        self.msg = QMessageBox ()
        self.msg.setIcon ( QMessageBox.Warning )
        self.msg.setWindowTitle ( "Warning" )
        self.msg.setText ( "Your choose wrong data", )



    def show_prof(self):
        self.msg.show()

class Warning_train( QtWidgets.QMainWindow ):
    def __init__(self, parent = None):
        super(Warning_train, self).__init__(parent)
        self.app = QApplication ( sys.argv )
        self.msg = QMessageBox ()
        self.msg.setIcon ( QMessageBox.Warning )
        self.msg.setWindowTitle ( "Warning" )
        self.msg.setText ( "Your choose same city", )



    def show_prof(self):
        self.msg.show()



class Addinfo( QtWidgets.QMainWindow ):
    def __init__(self, parent = None):
        super(Addinfo, self).__init__(parent)

        self.ui_add = uic.loadUi( "add_info_w.ui" )
        self.text1=self.ui_add.lineEdit


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





