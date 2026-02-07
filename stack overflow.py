from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.uic import loadUi
import sys

class MainUI(QMainWindow):
    
    def __init__(self):
        super(MainUI, self).__init__()

        # Load interface
        loadUi ("window1.ui", self)

        self.disable_interface()
        self.pushButton.clicked.connect(self.open_window)
        self.pushButton_2.clicked.connect(self.disconnect)


    def open_window (self):
        window2.show()

    def close__window (self):
        window2.close()

    def disable_interface (self):
        window2.close()

    def disconnect (self):
        self.disable_interface()

class SecondUI(QMainWindow):
    
    def __init__(self):
        super(SecondUI, self).__init__()

        # Load interface
        loadUi ("window2.ui", self)

if __name__ == "__main__":
    
   
    app = QApplication (sys.argv)
    window = MainUI()
    window2 = SecondUI()
    window.show()
    app.exec_()