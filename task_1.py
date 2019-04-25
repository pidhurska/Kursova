import sys
from PyQt5 import QtWidgets, QtCore, uic


class MainWWindow( QtWidgets.QMainWindow ):
    def __init__(self, parent = None):
        super(MainWWindow, self).__init__(parent)
        self.ui = uic.loadUi("main_w.ui")
        self.oImage = QtWidgets.QWidget.QImage( "UI1.jpg" )
        self.sImage = self.oImage.scaled ( QtWidgets.QWidget.QSize ( self.window_height, self.window_width ) )
        self.palette = QtWidgets.QWidget.QPalette ()
        self.palette.setBrush ( QtWidgets.QWidget.QPalette.Window, QtWidgets.QWidget.QBrush ( self.sImage ) )
        self.setPalette ( self.palette )
        self.sasw()
        self.ui.show()
    def sasw(self):
        self.password = self.ui.lineEdit_2
        self.password.setEchoMode(2)

if __name__ == '__main__':
    app = QtWidgets.QApplication ( sys.argv )
    window = MainWWindow()
    sys.exit ( app.exec () )