import sys
from PyQt5 import QtWidgets, QtCore, uic
import pymongo
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5 import QtWidgets, QtCore, uic

from PyQt5.QtCore import *
from Kursova.mes import *
from Kursova.feed_w import *
from Kursova.test_my import *
from Kursova.choose_ticket import *



class MainPWindow( QtWidgets.QMainWindow ):
    def __init__(self, parent = None):
        super(MainPWindow, self).__init__(parent)
        self.ui_profile = uic.loadUi( "profile.ui" )
        self.ui_add_info = Addinfo(self)
        self.feed = Feed(self)
        self.ui_test = MyTest(self)
        self.ui_ckoose_t = Choose_t(self)
        self.start_test = self.ui_profile.pushButton_5
        self.start_test.clicked.connect(self.ui_test.show_prof)



        sls = "mongodb+srv://Anastasia:20000103n!@cluster0-voyl5.mongodb.net/test?retryWrites=true&ssl_match_hostname=false&ssl_cert_reqs=CERT_NONE"
        self.client = pymongo.MongoClient ( sls )
        self.base1 = self.client.My_mogo
        self.base = self.base1.My_mogo

        """Read data from log ui"""
        f = open ( 'logdata.txt', 'r' )
        self.my_client = f.read()
        f.close ()

        """4 main button"""
        self.feedback = self.ui_profile.pushButton_4
        self.feedback.clicked.connect(self.feed.show_f)

        self.choose_t = self.ui_profile.pushButton_2
        self.choose_t.clicked.connect ( self.ui_ckoose_t.show_f)

        self.my_t = self.ui_profile.pushButton_3

        """My veraibles for prog"""
        self.info_db  = ""
        self.facebook = ""
        self.instagram = ""
        self.linkedin = ""
        self.photo = ""

        self.my_data()



    def my_inform(self):
        #For photo
        self.foto = self.ui_profile.label
        pixmap = QPixmap(self.photo)
        myScaledPixmap = pixmap.scaled ( self.foto.size (), Qt.KeepAspectRatio )
        self.foto.setPixmap ( myScaledPixmap )
        self.ui_profile.label_2.setText(str(self.info_db))

        #for links

        facebook_url = '<a href='+str(self.facebook)+'>Facebook</a>'
        instagram_url = '<a href='+str(self.instagram)+'>Instagram</a>'
        linkedin_url = '<a href='+str(self.linkedin)+'>Linkedin/a>'
        self.label3 = self.ui_profile.label_3
        self.label3.setText(facebook_url)
        self.label3.setOpenExternalLinks ( True )

        self.label4 = self.ui_profile.label_4
        self.label4.setText ( instagram_url)
        self.label4.setOpenExternalLinks ( True )

        self.label5 = self.ui_profile.label_5
        self.label5.setText (linkedin_url)
        self.label5.setOpenExternalLinks ( True )



    def my_data(self):
        for client in self.base.find({"Login": str(self.my_client)}):
            self.info_db = client["Name"] + "  " + client["Surname"] + "  " + client["Years"] + "  " + "years"
            self.photo = client["Photo"]
            self.facebook = client["Facebook"]
            self.instagram = client["Instagram"]
            self.linkedin = client["Linkedin"]
            self.my_inform()


    def show_prof(self):
        self.ui_profile.show()











