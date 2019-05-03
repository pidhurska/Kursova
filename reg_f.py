import sys
from PyQt5 import QtWidgets, QtCore, uic
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import pymongo
import datetime


class MainWWindow( QtWidgets.QMainWindow ):
    def __init__(self, parent = None):
        super(MainWWindow, self).__init__(parent)
        self.ui = uic.loadUi("reg_w.ui")
        self.test = 0
        self.form()
        self.ui.show()

    """Open directory for photo"""
    def openFile(self):
        self.fileD = QFileDialog.getOpenFileName(self,"Open file",'/', "*.jpg *.png")

    def form(self):
        self.ui.pushButton_3.clicked.connect(self.openFile)
        """All for mongodb"""
        sls = "mongodb+srv://Anastasia:20000103n!@cluster0-voyl5.mongodb.net/test?retryWrites=true&ssl_match_hostname=false&ssl_cert_reqs=CERT_NONE"
        self.client = pymongo.MongoClient (sls)
        self.db = self.client.My_mogo
        self.db2 = self.db.My_mogo
        "Text from buttons"
        self.button = self.ui.pushButton_2
        self.login = self.ui.lineEdit_8
        self.name = self.ui.lineEdit_4
        self.surname = self.ui.lineEdit_3
        self.password = self.ui.lineEdit
        self.facebook = self.ui.lineEdit_5
        self.instagram = self.ui.lineEdit_6
        self.linkedin = self.ui.lineEdit_7
        self.button.clicked.connect ( self.on_click )


    def adge(self):
        temp_var = self.ui.dateEdit.date ()
        nowd = datetime.date.today()
        nowy = nowd.year
        pre = temp_var.toPyDate()
        pre2 = pre.year
        years = int(nowy) - int(pre2)
        print(nowy, pre2 , years)
        self.date_b = years

    def mes_war(self):
        app = QApplication ( sys.argv )
        msg = QMessageBox ()
        msg.setIcon ( QMessageBox.Warning )
        msg.setWindowTitle ( "Warning" )
        msg.setText ( "You didn`t fill all entry fields" )
        msg.setStandardButtons ( QMessageBox.Ok )
        retval = msg.exec_ ()




    def on_click(self):
        deck = []
        self.adge()
        textboxValue_l = self.login.text()
        textboxValue_p = self.password.text()
        textboxValue_n = self.name.text()
        textboxValue_s = self.surname.text()
        textboxValue_f = self.facebook.text()
        textboxValue_i = self.instagram.text()
        textboxValue_lki = self.linkedin.text()
        textboxValue_d = self.date_b
        deck.append(textboxValue_l)
        deck.append(textboxValue_p)
        deck.append(textboxValue_n)
        deck.append(textboxValue_s)
        deck.append(textboxValue_f)
        deck.append(textboxValue_i)
        deck.append(textboxValue_lki)
        deck.append(textboxValue_d)
        for i in range(len(deck)):
            if deck[i] == "":
                self.mes_war()
                i+=1
            else:
                self.doc = {"Login": str(textboxValue_l), "Password": str(textboxValue_p),"Name": str(textboxValue_n),
                            "Surname": str(textboxValue_s),"Facebook": str(textboxValue_f),"Instagram": str(textboxValue_i),
                            "Linkedin": str(textboxValue_lki),"Years": str(textboxValue_d)}
                self.post_id = self.db2.insert_one ( self.doc ).inserted_id





if __name__ == '__main__':
    app = QtWidgets.QApplication ( sys.argv )
    window = MainWWindow()
    sys.exit ( app.exec () )