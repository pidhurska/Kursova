import sys
from PyQt5 import QtWidgets, QtCore, uic
import pymongo
from PyQt5 import QtGui
from PyQt5 import QtWidgets, QtCore, uic
from Kursova.prof_w import *
from Kursova.choose_ticket import *
from PyQt5.QtCore import *

class Feed( QtWidgets.QMainWindow ):
    def __init__(self, parent=None):
        super ( Feed, self ).__init__ ( parent )
        self.ui_feed = uic.loadUi ( "feedback_w.ui" )

        #setImage
        palette = QtGui.QPalette()
        self.image = QtGui.QImage("UI1_1.jpg")
        a = self.image.scaled(self.ui_feed.size())
        palette.setBrush(QtGui.QPalette.Window, QtGui.QBrush(a))
        self.ui_feed.setPalette(palette)

        self.prof = self.ui_feed.pushButton
        self.prof.clicked.connect (self.ui_feed.hide)

        self.buy_tick = self.ui_feed.pushButton_2
        self.buy_tick.clicked.connect ( self.ui_feed.hide)

        self.my_tick = self.ui_feed.pushButton_3
        self.my_tick.clicked.connect ( self.ui_feed.hide)

    def show_f(self):
        self.ui_feed.show()











