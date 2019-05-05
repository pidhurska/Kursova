import sys
from PyQt5 import QtWidgets, QtCore, uic
from Kursova.reg_f import *
from Kursova.prof_w import *
from Kursova.mes import *
import pymongo


class MainWWindow( QtWidgets.QMainWindow ):
    def __init__(self, parent = None):
        super(MainWWindow, self).__init__(parent)
        self.ui_main_w = uic.loadUi( "main_w.ui" )
        self.reg = MainRWindow(self)
        self.prof = MainPWindow(self)
        self.war = Warning_drl(self)


        sls = "mongodb+srv://Anastasia:20000103n!@cluster0-voyl5.mongodb.net/test?retryWrites=true&ssl_match_hostname=false&ssl_cert_reqs=CERT_NONE"
        self.client = pymongo.MongoClient ( sls )
        self.base1 = self.client.My_mogo
        self.base = self.base1.My_mogo

        self.login = self.ui_main_w.pushButton
        self.registration = self.ui_main_w.pushButton_2
        self.registration.clicked.connect (self.reg.show_my_reg)

        self.password_lo = self.ui_main_w.lineEdit_2
        self.password_lo.setEchoMode ( 2 )
        self.login.clicked.connect(self.onclick)

        self.ui_main_w.show()



    def onclick(self):

        self.password_log = self.password_lo.text ()
        self.login_lo = self.ui_main_w.lineEdit
        self.login_log = self.login_lo.text ()

        self.test = 0
        self.count_log =  self.base.find({"Login": str ( self.login_log)}).count()
        self.count_pass = self.base.find ({"Password": str ( self.password_log )} ).count ()
        if self.count_log== 0 or self.count_pass == 0:
            self.test = self.war.show_prof()
        else:
            self.test = self.prof.show_prof()
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