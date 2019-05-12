import sys
from PyQt5 import QtWidgets, QtCore, uic
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap
import pymongo
import datetime
from Kursova.mes import *
from PyQt5 import QtGui


class MainRWindow( QtWidgets.QMainWindow ):
    def __init__(self, parent = None):
        super(MainRWindow, self).__init__(parent)

        self.test = 0
        self.ui_reg_w = uic.loadUi( "reg_w.ui" )

        # setImage
        palette = QtGui.QPalette ()
        self.image = QtGui.QImage ( "UI1_1.jpg" )
        a = self.image.scaled ( self.ui_reg_w.size () )
        palette.setBrush ( QtGui.QPalette.Window, QtGui.QBrush ( a ) )
        self.ui_reg_w.setPalette ( palette )


        self.textboxValue_l =" "
        self.textboxValue_p =" "
        self.textboxValue_n =" "
        self.textboxValue_s =" "
        self.textboxValue_f =" "
        self.textboxValue_i =" "
        self.textboxValue_lki=" "
        self.textboxValue_d =" "
        self.war = Warning_d( self )
        self.war2 = Warning_a(self)

        self.photo = "/Users/anastasiapidgurska/університет/ТП/Kursova/?photo.png"
        self.setPhoto()
        self.form()




        """All for mongodb"""
        sls = "mongodb+srv://Anastasia:20000103n!@cluster0-voyl5.mongodb.net/test?retryWrites=true&ssl_match_hostname=false&ssl_cert_reqs=CERT_NONE"
        self.client = pymongo.MongoClient ( sls )
        self.db = self.client.My_mogo
        self.db2 = self.db.My_mogo

    """for enother window"""
    def show_my_reg(self):
        self.ui_reg_w.show()

    """Open directory for photo"""
    def openFile(self):
        self.fileD = QFileDialog.getOpenFileName(self,"Open file",'/', "*.jpg *.png")
        self.photo = self.fileD[0]
        self.setPhoto()

    def setPhoto(self):
        self.foto = self.ui_reg_w.label_9
        pixmap = QPixmap ( self.photo )
        myScaledPixmap = pixmap.scaled ( self.foto.size (), Qt.KeepAspectRatio )
        self.foto.setPixmap ( myScaledPixmap )


    def form(self):
        self.ui_reg_w.pushButton_3.clicked.connect( self.openFile )
        "Text from buttons"

        self.button = self.ui_reg_w.pushButton_2
        self.login = self.ui_reg_w.lineEdit_8
        self.name = self.ui_reg_w.lineEdit_4
        self.surname = self.ui_reg_w.lineEdit_3
        self.password = self.ui_reg_w.lineEdit
        self.password.setEchoMode (2 )
        self.facebook = self.ui_reg_w.lineEdit_5
        self.instagram = self.ui_reg_w.lineEdit_6
        self.linkedin = self.ui_reg_w.lineEdit_7
        self.button.clicked.connect ( self.on_click )



    def adge(self):
        temp_var = self.ui_reg_w.dateEdit.date ()
        nowd = datetime.date.today()
        nowy = nowd.year
        pre = temp_var.toPyDate()
        pre2 = pre.year
        years = int(nowy) - int(pre2)
        self.date_b = years




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
        self.count_log = self.db2.find ( {"Login": str ( self.textboxValue_l )} ).count ()
        self.test = 0
        if self.count_log == 0:
            for i in range(len(deck)-4):
                string = "".join (deck[i].split () )
                if len ( string ) > 3:
                    self.test+=1
                else:
                    self.war.show_prof()
                    break
        else:
            self.war2.show_prof()
        if self.test == 4:
            """Add data to mongodb"""
            self.doc = {"Login": str ( self.textboxValue_l ), "Password": str ( self.textboxValue_p ),
                        "Name": str ( self.textboxValue_n ),
                        "Surname": str ( self.textboxValue_s ), "Facebook": str ( self.textboxValue_f ),
                        "Instagram": str ( self.textboxValue_i ),"Linkedin": str ( self.textboxValue_lki ),
                        "Years": str ( self.textboxValue_d ), "Photo": str(self.photo),"Test": " ","Tickets" : " "}
            self.post_id = self.db2.insert_one ( self.doc ).inserted_id


            self.trains = {"Train1": "NKI608","Time": " ", "Price": "100"}
            self.post_id2 = self.db2.insert_one ( self.trains).inserted_id

            self.ui_reg_w.close()
        else:
            self.war.show_prof ()


