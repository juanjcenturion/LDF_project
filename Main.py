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

        #Import Logo.png.
        logo= QPixmap("Resources/logo.png")
        iconLabel.setPixmap(logo)
        
        #Scaling for logo.
        iconLabel.setScaledContents(True)
        
        #Add Qlabel whit Widget.
        upperLayout.addWidget(iconLabel)
        
        #Add layout to frame.
        self.frame1.setLayout(upperLayout)


        #-------------------------------------------------------
        
        #Frame Buttons whit horizontal layout.
        
        #Define frame settings.
        self.frame2=QFrame(self)
        self.frame2.setGeometry(0,80,480, 100)
        
        #Create "Button Panel" layout.
        button_panel= QHBoxLayout() 
        addProducts = Button("AGREGAR PRODUCTO", fontS= 10,fontF= "Ubuntu Mono Bold", foreg= self.bottontextcolor,backg= "#00FCA8", radius=11) #Create button.
        button_panel.addWidget(addProducts)                                                                               #Add button to layout.
        showCart = Button('VER MI CARRITO', fontS= 10,fontF= "Ubuntu Mono Bold",foreg= self.bottontextcolor,backg= "#1ADDF9", radius=11)       #Create Button.
        button_panel.addWidget(showCart)                                                                                  #Add button to layout.
        
        #Connect buttons to Functions.
        showCart.clicked.connect(self.openWindow)
        addProducts.clicked.connect(self.addToCart)

        
        #Add layout to Frame.
        self.frame2.setLayout(button_panel)
        

        #---------------------------------------------

if __name__ == '__main__':                      #App Execution.
    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec()