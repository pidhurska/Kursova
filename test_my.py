import sys
from PyQt5 import QtWidgets, QtCore, uic

import pymongo
class MyTest( QtWidgets.QMainWindow ):
    def __init__(self, parent = None):
        super(MyTest, self).__init__(parent)

        sls = "mongodb+srv://Anastasia:20000103n!@cluster0-voyl5.mongodb.net/test?retryWrites=true&ssl_match_hostname=false&ssl_cert_reqs=CERT_NONE"
        self.client = pymongo.MongoClient ( sls )
        self.base1 = self.client.My_mogo
        self.base = self.base1.My_mogo

        self.ui_test = uic.loadUi( "test_w.ui" )
        self.sfears = ["AGRARIAN", "SECURITY","MILITARY", "IT","SPACE AND AVIATION", "BEAUTY AND FASHION", "LIGHT INDUSTRY", "LINGUISTIC","LOGISTICS, FEA, TRADE", "MEDICAL","SEA","SCIENCE","PEDAGOGICAL","FOOD INDUSTRY","POLICY AND STATE SERVICE","WORK WITH PEOPLE","RELATED TO ANIMALS","RELATED TO TRAVEL","MEDIA AND PUBLISHING HOUSE","CREATIVE","SPORT","TECHNICAL","TRANSPORT","ECONOMIC","LEGAL"]
        self.bookj =["Fantasy","Science Fiction","Westerns","Romance","Thriller","Mystery","Detective story","Dystopia","Other"]
        self.filmj =["Action", "Adventure", "Comedy","Crime&Gangsters", "Drama", "Epic", "Horror", "Science fiction","War","Other"]
        self.hobbyj = ["Fishkeeping","Learning","Meditation","Reading","Shortwave listening","Audiophile","Videophilia","Birdwatching","Bus spotting","Photography","Travelin","Sport","Playing on musical instruments ","Other"]
        self.pizzat= ["Margherita","Marinara","Quattro Stagioni","Carbonara","Quattro Formaggi","Crudo","Napoli","Other"]
        self.spanget = ["SpongeBob SquarePants", "Squidward Tentacles","Sandy Cheeks","Patrick Star","Eugene H. Krabs","Sheldon J. Plankton","Princess Mindy","Mrs. Puff"]

        self.btnok = self.ui_test.pushButton
        self.list_val = " "
        f = open ('cities.txt', 'r' )

        self.city_list1 = f.read()
        f.close ()
        self.city_list = self.city_list1.split(",")

        #combo boxes
        self.cities = self.ui_test.comboBox
        self.cities.setEditable ( True )
        self.cities.addItems (self.city_list)

        self.sphere = self.ui_test.comboBox_2
        self.sphere.setEditable ( True )
        self.sphere.addItems (self.sfears)

        self.book = self.ui_test.comboBox_3
        self.book.setEditable ( True )
        self.book.addItems (self.bookj)

        self.film = self.ui_test.comboBox_4
        self.film.setEditable ( True )
        self.film.addItems ( self.filmj)

        self.hobby = self.ui_test.comboBox_5
        self.hobby.setEditable ( True )
        self.hobby.addItems ( self.hobbyj)

        self.talent = self.ui_test.comboBox_6
        self.talent.setEditable ( True )
        self.talent.addItems (["Art","Sing","Dance","Play","Sport","Write","Sport","Other"])

        self.drink = self.ui_test.comboBox_7
        self.drink.setEditable ( True )
        self.drink.addItems (["Tea","Coffee","Water","Other"])

        self.pets = self.ui_test.comboBox_8
        self.pets.setEditable ( True )
        self.pets.addItems (["Dog","Cat","Hamster"])

        self.activity = self.ui_test.comboBox_9
        self.activity.setEditable ( True )
        self.activity.addItems (["Active","Passive"])

        self.season = self.ui_test.comboBox_10
        self.season.setEditable ( True )
        self.season.addItems (["Wither","Spring","Summer","Autumn"])

        self.pizza = self.ui_test.comboBox_11
        self.pizza.setEditable ( True )
        self.pizza.addItems (self.pizzat)

        self.spangeBob = self.ui_test.comboBox_12
        self.spangeBob.setEditable ( True )
        self.spangeBob.addItems (self.spanget)

        self.btnok.clicked.connect(self.on_click)


    def additional(self):
        f = open ( 'logdata.txt', 'r' )
        self.my_client = f.read ()
        for i in self.base.find({"Login": str(self.my_client)}):
            self.base.update ({},{"$set":{"Test": str(self.list_val)} })
        f.close ()
    def on_click(self):
        c = self.cities.currentText()
        s = self.sphere.currentText ()
        b = self.book.currentText ()
        f = self.film.currentText ()
        h = self.hobby.currentText ()
        t = self.talent.currentText ()
        d = self.drink.currentText ()
        p = self.pets.currentText ()
        a = self.activity.currentText ()
        seas = self.season.currentText ()
        pizz = self.pizza.currentText ()
        spang = self.cities.currentText ()
        self.list_val = [c,s,b,f,h,t,d,p,a,seas,pizz,spang]
        self.additional()
        self.ui_test.hide()
        print(self.list_val)



    def show_prof(self):
        self.ui_test.show ()