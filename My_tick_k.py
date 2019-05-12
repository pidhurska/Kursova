
import pymongo

from PyQt5 import QtWidgets, QtCore, uic
from PyQt5 import QtGui

class Show_t( QtWidgets.QMainWindow ):
    def __init__(self, parent=None):
        super ( Show_t, self ).__init__ ( parent )
        self.ui_sh = uic.loadUi ( "My_tick_w.ui" )

        # setImage
        palette = QtGui.QPalette ()
        self.image = QtGui.QImage ( "UI1_1.jpg" )
        a = self.image.scaled ( self.ui_sh.size () )
        palette.setBrush ( QtGui.QPalette.Window, QtGui.QBrush ( a ) )
        self.ui_sh.setPalette ( palette )

        self.my_ntext = ""
        sls = "mongodb+srv://Anastasia:20000103n!@cluster0-voyl5.mongodb.net/test?retryWrites=true&ssl_match_hostname=false&ssl_cert_reqs=CERT_NONE"
        self.client = pymongo.MongoClient ( sls )
        self.base2 = self.client.My_mogo
        self.base_t = self.base2.My_mogo

        f = open ( 'logdata.txt', 'r' )
        self.list = f.read ()
        self.list_data = self.list.split ( "," )
        f.close ()
        for client in self.base_t.find({str(self.list_data[0]):str(self.test)}):
            self.my_ntext = client["Ticket"]

        self.lable_qwe = self.ui_sh.lable
        self.lable_qwe.setText(self.my_ntext)

        self.prof = self.ui_feed.pushButton
        self.prof.clicked.connect (self.ui_sh.hide)

        self.buy_tick = self.ui_feed.pushButton_2
        self.buy_tick.clicked.connect ( self.ui_sh.hide)

        self.feed = self.ui_feed.pushButton_4
        self.feed.clicked.connect ( self.ui_sh.hide)


    def show_f(self):
        self.ui_feed.show()