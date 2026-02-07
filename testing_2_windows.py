#
# -------------------------------------------
# Send suggestions at cristian.buru@gmail.com
# -------------------------------------------
#

from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.uic import loadUi

from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtCore import QRegExp

import sys


class MainUI(QMainWindow):
    def __init__(self):
        super(MainUI, self).__init__()

        # Load interface
        loadUi ("window1.ui", self)

        self.pushButton.clicked.connect (self.open_window)

    def open_window (self):
        self.second = SecondUI()
        self.second.show()
        print ("Open second window")


class SecondUI(QMainWindow):
    def __init__(self):
        super(SecondUI, self).__init__()

        # Load interface
        loadUi ("window2.ui", self)
        

  

if __name__ == "__main__":
    
   

    # Enable High DPI display with PyQt5
    QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
    # QApplication.setHighDpiScaleFactorRoundingPolicy (QtCore.Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    QApplication.setHighDpiScaleFactorRoundingPolicy (QtCore.Qt.HighDpiScaleFactorRoundingPolicy.Ceil)
    
    app = QApplication (sys.argv)
    window = MainUI()
    window.show()
    app.exec_()