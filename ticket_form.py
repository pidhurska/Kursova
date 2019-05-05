
from PyQt5 import QtWidgets, QtCore, uic

import pymongo


class order_my( QtWidgets.QMainWindow ):
    def __init__(self, parent=None):
        super ( order_my, self ).__init__ ( parent )
        self.ui_1 = uic.loadUi ( "form_buy.ui" )

        sls = "mongodb+srv://Anastasia:20000103n!@cluster0-voyl5.mongodb.net/test?retryWrites=true&ssl_match_hostname=false&ssl_cert_reqs=CERT_NONE"
        self.client = pymongo.MongoClient ( sls )
        self.base1 = self.client.My_mogo
        self.base = self.base1.My_mogo


        f = open ( 'logdata.txt', 'r' )
        self.list = f.read()
        self.list_data = self.list.split(",")
        print(self.list_data)
        if len(self.list_data) < 5:
            self.my_client = self.list_data[0]
            self.data_m = self.list_data[1]
            self.city1 = self.list_data[2]
            self.city2 = self.list_data[3]







    def show_f(self):
        self.ui_1.show ()











