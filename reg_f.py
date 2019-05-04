import sys
from PyQt5 import QtWidgets, QtCore, uic
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap
import pymongo
import datetime


class MainRWindow( QtWidgets.QMainWindow ):
    def __init__(self, parent = None):
        super(MainRWindow, self).__init__(parent)
        self.test = 0
        self.ui = uic.loadUi("reg_w.ui")
        self.form()


        """All for mongodb"""
        sls = "mongodb+srv://Anastasia:20000103n!@cluster0-voyl5.mongodb.net/test?retryWrites=true&ssl_match_hostname=false&ssl_cert_reqs=CERT_NONE"
        self.client = pymongo.MongoClient ( sls )
        self.db = self.client.My_mogo
        self.db2 = self.db.My_mogo

    """for enother window"""
    def show_my_reg(self):
        self.ui.show()

    """Open directory for photo"""
    def openFile(self):
        self.fileD = QFileDialog.getOpenFileName(self,"Open file",'/', "*.jpg *.png")
        self.photo = self.fileD[0]
        self.foto = self.ui.label_9
        pixmap = QPixmap( self.photo )
        myScaledPixmap = pixmap.scaled ( self.foto.size (), Qt.KeepAspectRatio )
        self.foto.setPixmap ( myScaledPixmap )


    def form(self):
        self.ui.pushButton_3.clicked.connect(self.openFile)

        "Text from buttons"

        self.button = self.ui.pushButton_2
        self.login = self.ui.lineEdit_8
        self.name = self.ui.lineEdit_4
        self.surname = self.ui.lineEdit_3
        self.password = self.ui.lineEdit
        self.password.setEchoMode (2 )
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
        msg.setText ( "You did not fill right entry fields \n Your string must content min 6 characters", )
        msg.setStandardButtons ( QMessageBox.Ok )
        retval = msg.exec_ ()


    def on_click(self):
        deck = []
        self.adge()
        self.textboxValue_l = self.login.text()
        self.textboxValue_p = self.password.text()
        self.textboxValue_n = self.name.text()
        self.textboxValue_s = self.surname.text()
        self.textboxValue_f = self.facebook.text()
        self.textboxValue_i = self.instagram.text()
        self.textboxValue_lki = self.linkedin.text()
        self.textboxValue_d = self.date_b
        deck.append(self.textboxValue_l)
        deck.append(self.textboxValue_p)
        deck.append(self.textboxValue_n)
        deck.append(self.textboxValue_s)
        deck.append(self.textboxValue_f)
        deck.append(self.textboxValue_i)
        deck.append(self.textboxValue_lki)
        deck.append(self.textboxValue_d)
        self.test = 0
        for i in range(len(deck)-4):
            string = "".join (deck[i].split () )
            print(string)
            if len ( string ) > 6:
                self.test+=1
            else:
                self.mes_war()
                break
        if self.test == 4:
            """Add data to mongodb"""
            self.doc = {"Login": str ( self.textboxValue_l ), "Password": str ( self.textboxValue_p ),
                        "Name": str ( self.textboxValue_n ),
                        "Surname": str ( self.textboxValue_s ), "Facebook": str ( self.textboxValue_f ),
                        "Instagram": str ( self.textboxValue_i ),
                        "Linkedin": str ( self.textboxValue_lki ), "Years": str ( self.textboxValue_d ),
                        "Photo": str(self.photo)}
            #self.post_id = self.db2.insert_one ( self.doc ).inserted_id

            self.ui.close()
        else:
            self.form()


