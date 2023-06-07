#Imports.
import os, sys
sys.path.append(os.path.abspath('Resources'))

from datetime import datetime
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from Resources.styles_normalize import Text,Input,Button
from controller import*

class WindowThree(QMainWindow):                 #Window 3 - calculate and pay.
    def _init_(self):
        super()._init_()
        
        
        #Window properties - 1. Title - 2.Style - 3. Fixed size.
        self.setWindowTitle("SubStore - Sistema de pago.")
        self.setStyleSheet("background-color: #272727;")
        self.setFixedSize(QSize(480, 480))

        #-----------------------------------------------------------

        #Frame Title/Header whit Vertical Layout.

        #Define Frame Settings.
        self.frame1= QFrame(self)
        self.frame1.setGeometry(57,30,368,105)
        
        #Create layout.
        upperLayout =QVBoxLayout() 
        #QLabel creation to store icon.
        iconLabel= QLabel(self)
        #Import Logo.png.
        logo= QPixmap("Resources/pagos.png")
        iconLabel.setPixmap(logo)
        #Scaling for logo.
        iconLabel.setScaledContents(True)
        #Add Qlabel whit Widget.
        upperLayout.addWidget(iconLabel)
        
        #Add layout to frame.
        self.frame1.setLayout(upperLayout)

        #----------------------------------------------------------

        #Frame list of products add to cart whit vertical layout.
        
        #Define frame settings.
        self.frame2= QFrame(self)
        self.frame2.setGeometry(0, 140, 480, 620)

        #Define other Frames
        self.frame2Layout= QVBoxLayout()
        self.frame2QFL= QFormLayout()

        self.subtotal= 0

        self.phonecartList= readCart()
        for phone in self.phonecartList:
            self.subtotal+= phone[1]

        #------------------------------------------------------------

        # Calculate total.

        #Icome Tax - IVA And conversion to local money whith icome.
        icomeIVA= 1.21
        icomePAIS= 1.30
        priceTuristDollar= 490
        priceDollar= 155
        if self.subtotal >= 300: 
            self.total= (round(((self.subtotal * icomeIVA)*icomePAIS),2))
            self.totalPesoArgentino = round(self.total * priceTuristDollar, 2)
        else:
            self.total= (round(((self.subtotal * icomeIVA)*icomePAIS),2))
            self.totalPesoArgentino= round(self.total * priceDollar, 2)
            
        #---------------------------------------------------------------------------

class WindowTwo(QMainWindow):                   #Window 2 - Shopping Cart prosecution.
    def __init__(self):
        super().__init__()
       
        #Window properties - 1. Title - 2.Style - 3. Fixed size.
        self.setWindowTitle("SubStore - Carrito de compras.")
        self.setStyleSheet("background-color: #272727;")
        self.setFixedSize(QSize(480, 720))
       
        #------------------------------------------------------

        #Frame Title/Header whit Vertical Layout.

        #Define Frame Settings.
        self.frame1= QFrame(self)
        self.frame1.setGeometry(57,30,368,105)
       
        #Create layout.
        upperLayout =QVBoxLayout()

        #QLabel creation to store icon.
        iconLabel= QLabel(self)

        #Import Logo.png.
        logo= QPixmap("Resources/carry.png")
        iconLabel.setPixmap(logo)
       
        #Scaling for logo.
        iconLabel.setScaledContents(True)

        #Add Qlabel whit Widget.
        upperLayout.addWidget(iconLabel)
       
        #Add layout to frame.
        self.frame1.setLayout(upperLayout)


        #--------------------------------------------------------   
    #Frame list of products add to cart whit vertical layout.

        #Define frame settings.
        self.frame2= QFrame(self)
        self.frame2.setGeometry(0, 140, 480, 620)
        
        #Define other Frames
        self.frame2Layout= QVBoxLayout()
        
        self.frame2QFL= QFormLayout()

        
        

        #Subtotal: Phone shell.

        self.subTotal=0
        
        #Read Cart from phonesDb.

        self.phonecartList= readCart()
        for phone in self.phonecartList:       
            #Create QLabel from each selected phone.

            self.textbx=Text(f"{phone[0]}",fontS= 13,fontF= "Italic", backg= "#272727", foreg= "#F8F8FF",hAlign="aT", vAlign= "aT")
            self.priceStr= Text(f"U$D {phone[1]}",fontS= 13,fontF= "Italic", backg= "#272727", foreg= "#F8F8FF",hAlign="aR", vAlign= "aT")
            
            #Add Labels to QFromLayout.
            self.frame2QFL.addRow(self.textbx, self.priceStr)
            
            # Addition to subtotal.
            self.subTotal+= phone[1]
        
        


        
        #Create SubTotal QLabel and SubTotal texts
        self.textSub= Text(f"SUBTOTAL:",fontS= 13,fontF= "Italic", backg= "#272727", foreg= "#F8F8FF", hAlign= "aT", vAlign= "aL")
        self.subtotal= Text(f"U$D {self.subTotal}",fontS= 13,fontF= "Italic", backg= "#272727", foreg= "#F8F8FF", hAlign= "aT", vAlign= "aR")
        self.textSub1 = Text(f"(Este valor no contiene impuestos.)",fontS= 5,fontF= "Arial Black", backg= "#272727", foreg= "#F8F8FF",hAlign= "aR", vAlign= "aR" )
        
        #Add Labels to QFormLayout
        self.frame2QFL.addRow(self.textSub, self.subtotal)
        self.frame2QFL.addRow("",self.textSub1)

        #Add QFormLayout to Vertical Layout
        self.frame2Layout.addLayout(self.frame2QFL)
        
        #Add layout to frames.
        self.frame2.setLayout(self.frame2Layout)

        #----------------------------------------------------------

        #Frame Button payments or return whit horizontal layout.
        
        #Define Frame Settings.
        self.frame3=QFrame(self)
        self.frame3.setGeometry(0,640,480, 80)

        #Create "Button Panel" layout.
        button_panel= QHBoxLayout()
        buttonClear = Button('LIMPIAR Y REGRESAR', fontS= 10,fontF= "Italic",foreg= "#272727",backg= "#00FCA8", radius=11)  #Create button.
        buttonPay = Button('IR A PAGOS', fontS= 10,fontF= "Italic",foreg= "#272727",backg= "#1ADDF9", radius=11)            #Create button.
        button_panel.addWidget(buttonClear)                                                                                 #Add button to layout.
        button_panel.addWidget(buttonPay)                                                                                   #Add button to layout.
        buttonClear.clicked.connect(self.clearCart)                                                                         #Connect button to function.
        buttonPay.clicked.connect(self.openPayments)                                                                        #Connect button to function.
        
        
        #Add layout to Frame.
        self.frame3.setLayout(button_panel)
    

    def openPayments(self):
        self.hide()
        #Window opening function 3 to add to cart.
        self.wThree = WindowThree()
        self.wThree.show()
    

    def clearCart(self):                        #Delete cart function, clear Database and Close Window to go back. 
        deleteCart()
        self.close()
        self.wMain= MainWindow()
        self.wMain.show()





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
     
      def addToCart(self):                                    #Function add products to shopping car and Count.
        #counter
        self.counter +=1 
        #Create List Cart.
        
        item= self.products.currentText()
        smartphone= item.split("$")
        strEnd= 2 + smartphone[0].find("gb")
        model, price = smartphone[0][0:strEnd], smartphone[1]
        #price= int(price[4:])
        createCartTable()
        insertProdToCart(model, price)

        productAddedMsgb = QMessageBox()

        productAddedMsgb.setGeometry(250,400, 240,240)
        productAddedMsgb.setStyleSheet(f"background-color: {self.colorback}; color: white ")
        productAddedMsgb.setText(f"Ha agregado el producto a su carrito.")
        productAddedMsgb.setFont(QFont("Ubuntu Mono Bold", 10))
        productAddedMsgb.setWindowTitle("Producto agregado!!")
        productAddedMsgb.setDefaultButton(QMessageBox.Ok)
        productAddedMsgb.exec()
        
        
    def openWindow(self):
        self.hide()
        #Window opening function 2 to add to cart.
        self.wTwo = WindowTwo()
        self.wTwo.show()
 



if __name__ == '__main__':                      #App Execution.
    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec()