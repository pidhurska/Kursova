import sys
from PyQt5 import QtWidgets, QtCore, uic

"Import moduls"
from Kursova.reg_f import *
from Kursova.prof_w import *
from Kursova.mes import *
import pymongo
from PyQt5 import QtGui


class MainWWindow( QtWidgets.QMainWindow ):
    def __init__(self, parent = None):
        super(MainWWindow, self).__init__(parent)
        self.ui_main_w = uic.loadUi( "main_w.ui" )
        self.reg = MainRWindow(self)
        self.prof = MainPWindow(self)
        self.war = Warning_drl(self)

        #setImage
        palette = QtGui.QPalette()
        self.image = QtGui.QImage("UI1_1.jpg")
        a = self.image.scaled(self.ui_main_w.size())
        palette.setBrush(QtGui.QPalette.Window, QtGui.QBrush(a))
        self.ui_main_w.setPalette(palette)

        #for connection to MongoDB
        sls = "mongodb+srv://Anastasia:20000103n!@cluster0-voyl5.mongodb.net/test?retryWrites=true&ssl_match_hostname=false&ssl_cert_reqs=CERT_NONE"
        self.client = pymongo.MongoClient ( sls )
        self.base1 = self.client.My_mogo
        self.base = self.base1.My_mogo

        # Set text data for login
        self.login = self.ui_main_w.pushButton
        self.registration = self.ui_main_w.pushButton_2

        #Act of clicked button "Registration"
        self.registration.clicked.connect (self.reg.show_my_reg)

        # Set text data for password
        self.password_lo = self.ui_main_w.lineEdit_2
        #Set no-visible data
        self.password_lo.setEchoMode ( 2 )
        #Button login
        self.login.clicked.connect(self.onclick)
        # Show interface
        self.ui_main_w.show()


    #Method onclick
    def onclick(self):
        #Get text fronm lines
        self.password_log = self.password_lo.text ()
        self.login_lo = self.ui_main_w.lineEdit
        self.login_log = self.login_lo.text ()

        self.test = 0
        # find login and password in Base
        self.count_log =  self.base.find({"Login": str ( self.login_log)}).count()
        self.count_pass = self.base.find ({"Password": str ( self.password_log )} ).count ()
        #raise error
        if self.count_log== 0 or self.count_pass == 0:
            self.test = self.war.show_prof()
        else:
            #if login and password are true open Profile interface
            self.test = self.prof.show_prof()
            #rebember login in file
            f = open ( 'logdata.txt', 'w' )
            f.write(self.login_log)
            f.close()
            self.ui_main_w.hide()

        return self.test





def main():
    app = QtWidgets.QApplication ( sys.argv )
    main = MainWWindow()
    sys.exit(app.exec_())

main()