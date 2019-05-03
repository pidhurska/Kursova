import sys
import sys
from PyQt5 import QtWidgets, QtCore, uic
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


def mes_war():
    app = QApplication ( sys.argv )
    msg = QMessageBox ()
    msg.setIcon ( QMessageBox.Warning )
    msg.setWindowTitle ( "Warning" )
    msg.setText ( "You didn`t fill all entry fields" )
    msg.setStandardButtons ( QMessageBox.Ok )
    retval = msg.exec_ ()





if __name__ == '__main__':
    mes_war ()