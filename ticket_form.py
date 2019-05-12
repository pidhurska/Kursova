
from PyQt5 import QtWidgets, QtCore, uic
from PyQt5 import QtGui
import pymongo


class order_my( QtWidgets.QMainWindow ):
    def __init__(self, parent=None):
        super ( order_my, self ).__init__ ( parent )
        self.ui_1 = uic.loadUi ( "form_buy.ui" )

        sls = "mongodb+srv://Anastasia:20000103n!@cluster0-voyl5.mongodb.net/test?retryWrites=true&ssl_match_hostname=false&ssl_cert_reqs=CERT_NONE"
        self.client = pymongo.MongoClient ( sls )
        self.base1 = self.client.My_mogo
        self.base = self.base1.My_mogo

        # setImage
        palette = QtGui.QPalette ()
        self.image = QtGui.QImage ( "UI1_1.jpg" )
        a = self.image.scaled ( self.ui_1.size () )
        palette.setBrush ( QtGui.QPalette.Window, QtGui.QBrush ( a ) )
        self.ui_1.setPalette ( palette )

        self.area_w = self.ui_1.label
        self.people_chat = " "

        self.client = " "
        self.data_m = " "
        self.city1 = " "
        self.city2 = " "
        self.test = " "
        self.my_seat = ""

        f = open ( 'logdata.txt', 'r' )
        self.list = f.read()
        self.list_data = self.list.split(",")
        f.close()

        print(self.list_data)
        if len(self.list_data) > 3:
            self.client = self.list_data[0]
            self.data_m = self.list_data[1]
            self.city1 = self.list_data[2]
            self.city2 = self.list_data[3]

        f = open ( 'seats.txt', 'r' )
        self.seat_list1 = f.read ()
        f.close ()
        self.seats_list = self.seat_list1.split ( "," )

        # combo boxes
        self.seats = self.ui_1.comboBox
        self.seats.setEditable ( True )
        self.seats.addItems ( self.seats_list)

        # lables

        self.ui_1.label_4.setText ( str ( "NYR843" ) )
        self.ui_1.label_6.setText ( str ( self.data_m ) + "    19-00" )
        self.ui_1.label_8.setText ( str ( "100 uah" ) )

        self.info()

        self.ui_1.pushButton.clicked.connect(self.write)

    def info(self):
        for my_client in self.base.find({"Login":str(self.client)}):
            self.test = my_client["Test"]
            if self.test != " ":
                for test in self.base.find({"Login":str(self.test)}):
                    self.people_chat = test["Name"] + " "+ test["Surname"] + " "+ test["Years"] + " "+ test["Facebook"]+ " "+ test["Instagram"]+ " "+ test["Linkedin"]+ " "+ test["Ticket"]
            self.area_w.setText(str(self.people_chat))

    def write(self):
        my_seat = self.seats.currentText()
        self.my_seat = str(self.data_m) + " " + "trin №: NYR843  price: 100 uah  seat: " + str(my_seat)
        self.new_m = self.seats_list

        """for i in range(len(self.seats_list)) :
            if my_seat == self.new_m[i]:
                self.new_m.pop(i)
        self.new_l = ','.join(map(str,self.new_m))

        f = open ( 'seats.txt', 'w' )
        f.write(self.new_l)
        f.close ()"""
        for client in self.base.find({"Login":str(self.test)}):
            self.base.update ( {}, {"$set": {"Ticket": str ( self.my_seat)}})
        self.ui_1.hide()















    def show_f(self):
        self.ui_1.show ()











