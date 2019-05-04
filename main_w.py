import sys
from PyQt5 import QtWidgets, QtCore, uic
from Kursova.reg_f import *

class MainWWindow( QtWidgets.QMainWindow ):
    def __init__(self, parent = None):
        super(MainWWindow, self).__init__(parent)
        self.ui = uic.loadUi("main_w.ui")
        self.reg = MainRWindow ( self )


        sls = "mongodb+srv://Anastasia:20000103n!@cluster0-voyl5.mongodb.net/test?retryWrites=true&ssl_match_hostname=false&ssl_cert_reqs=CERT_NONE"
        self.client = pymongo.MongoClient ( sls )
        self.base1 = self.client.My_mogo
        self.base = self.base1.My_mogo

        self.login = self.ui.pushButton
        self.registration = self.ui.pushButton_2
        self.registration.clicked.connect ( self.reg.show_my_reg )


        self.sasw()


        self.ui.show()


    def sasw(self):
        self.password_log = self.ui.lineEdit_2
        self.password_log.setEchoMode(2)
        self.password_log = self.password_log.text()
        self.login_log = self.ui.lineEdit
        self.login_log = self.login_log.text()
        self.login.clicked.connect (self.on_click)


    def on_click(self):
        if self.base.find({"Login": str(self.login_log)}).count() == 1:
            if self.base.find({"Password": str(self.password_log)}).count() == 1:
                print("ok")
            else:
                self.reg.mes_war()

        else:
            self.reg.mes_war()



def main():
    app = QtWidgets.QApplication ( sys.argv )
    main = MainWWindow()

    sys.exit(app.exec_())

main()