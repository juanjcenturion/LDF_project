#Imports.
import os, sys
sys.path.append(os.path.abspath('Resources'))

from datetime import datetime
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *


class MainWindow(QMainWindow):                  #Window 1 - Products addition to Shopping Cart
    def __init__(self):
        super().__init__()
        
        #mode Dark or light!
        now= datetime.now()
        self.hours= now.hour

        if self.hours >= 8 and self.hours < 20:
            self.colorback = "#546e7a"
            self.bottontextcolor= "#424242" 
        else:
            self.colorback= "#272727"
            self.bottontextcolor= "#272727"

        

        #Window properties - 1. Title - 2.Style - 3. Fixed size.
        self.setWindowTitle("SubStore - App de compras")
        self.setStyleSheet(f"background-color: {self.colorback}")
        self.setFixedSize(QSize(480, 480))
        
        #Frame Title/Header whit Vertical Layout.

        #Define Frame Settings.
        self.frame1= QFrame(self)
        self.frame1.setGeometry(56,0,368,105)
        
        #Create layout.
        upperLayout =QVBoxLayout() 

        #QLabel creation to store icon.
        iconLabel= QLabel(self)



if __name__ == '__main__':                      #App Execution.
    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec()