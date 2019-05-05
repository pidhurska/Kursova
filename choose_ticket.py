import sys
from PyQt5 import QtWidgets, QtCore, uic
import pymongo
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5 import QtWidgets, QtCore, uic
from Kursova.prof_w import *
from Kursova.mes import *
from Kursova.ticket_form import *
from PyQt5.QtCore import *
import datetime

class Choose_t( QtWidgets.QMainWindow ):
    def __init__(self, parent=None):
        super (Choose_t, self ).__init__ ( parent )
        self.chst = uic.loadUi ( "choose_t.ui" )
        self.ui_mes_c = Warning_city(self)
        self.ui_mes_d = Warning_data(self)
        self.ui_mes_notrain = Warning_train(self)

        self.order = order_my(self)
        # if we have no train
        self.no_train = 1

        self.prof = self.chst.pushButton
        self.prof.clicked.connect ( self.chst.hide )

        self.feed = self.chst.pushButton_2
        self.feed.clicked.connect ( self.chst.hide )

        self.my_tick = self.chst.pushButton_3
        self.my_tick.clicked.connect ( self.chst.hide )

        self.my_buy = self.chst.pushButton_5
        self.my_buy.clicked.connect (self.on_click)

        f = open ('cities.txt', 'r' )
        self.city_list1 = f.read()
        f.close ()
        self.city_list = self.city_list1.split(",")

        #combo boxes
        self.city1 = self.chst.comboBox
        self.city1.setEditable ( True )
        self.city1.addItems ( self.city_list )

        self.city2 = self.chst.comboBox_2
        self.city2.setEditable ( True )
        self.city2.addItems ( self.city_list )

    def date(self):
        self.temp_var = self.chst.dateEdit.date ()
        self.nowy = datetime.date.today()
        pre = self.temp_var.toPyDate()
        years = pre - self.nowy
        self.date_b = years.days

    def on_click(self):
        city1 = self.city1.currentText ()
        city2 = self.city2.currentText ()
        self.date()
        print(self.date_b)
        if city1 == city2:
            self.ui_mes_c.show_prof()
        elif self.date_b < 0:
            self.ui_mes_d.show_prof()
        elif self.no_train == 0:
            self.ui_mes_notrain.show_prof()
        else:
            f = open('logdata.txt', 'a' )
            data_my = "," +str(self.nowy)+","+str(city1)+","+str(city2)
            print(data_my)
            f.write(data_my)
            f.close()
            self.order.show_f()
            self.chst.hide()



    def show_f(self):
        self.chst.show()











