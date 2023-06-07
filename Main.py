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

        #Frame Combobox whit vertical layout for smartphones products.

        #Define frame settings.
        self.frame3= QFrame(self)
        self.frame3.setGeometry(0,150,480,100)
        
        #Create layout.
        frame3layout= QVBoxLayout()
        
        #Create and add items to Combobox.
        self.products = QComboBox()
        self.products.setPlaceholderText('Seleccione  un  producto')
        self.products.setStyleSheet("background-color: #808080; font-family: Ubuntu Mono;")
        self.products.setStyleSheet("color: #FFFFE0")
        
        
        def espacios(c):
            e =''
            for _ in range(c):
                e += " "
            return e

        #Data from database phones.- Celulares.db.
        phones_list= readRows()
        phoneNewList= []
        for phone in phones_list:
            
            cE =60 - len(phone[1])
            phonestr= phone[1] + espacios(cE) + phone[2]
            phoneNewList.append(phonestr)
    
        self.products.addItems(phoneNewList)         


        frame3layout.addWidget(self.products)                               #Add widget to layout.
        
        #Add layout to frame.
        self.frame3.setLayout(frame3layout)


        #---------------------------------------------------
        
        #Create variable count click.
        self.counter= 0 
        



if __name__ == '__main__':                      #App Execution.
    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec()