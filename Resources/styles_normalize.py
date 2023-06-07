from dataclasses import dataclass

from PySide6.QtWidgets import (
    QApplication, 
    QWidget, 
    QMainWindow, 
    QVBoxLayout,
    QLabel, 
    QLineEdit, 
    QPushButton
    )

from PySide6.QtGui import QFont
from PySide6.QtCore import Qt


@dataclass
class Widget:
    string: str = ""
    fontF: str = "Arial"
    fontS: int = 15
    foreg: str = "black"
    backg: str = "white"
    hAlign: str ="hC"
    vAlign: str ="vC"
    border: int = 0
    radius: int = 15

    def style(self, klass):
        align = {
            "aL": Qt.AlignLeft,
            "hC": Qt.AlignCenter,
            "aR": Qt.AlignRight,
            "aT": Qt.AlignTop, 
            "vC": Qt.AlignVCenter,
            "aB": Qt.AlignBottom
            }
        self.setText(str(self.string))

        sts = fr"""
            {klass} {{
            background-color: {self.backg}; 
            color: {self.foreg};
            padding: 5; 
            border: {self.border}px solid;
            border-radius: {self.radius}px;
        }}
        """
        
        if isinstance(self, Input):
            self.selectAll()
        if isinstance(self, Button):
            stf =  fr"""
            {klass}:focus {{
                outline: none;
                font-weight: 900;
            }}
            """
            sts += stf
        else:
            self.setAlignment(align[self.hAlign] | align[self.vAlign])
            
        self.setFont(QFont(self.fontF, self.fontS))
        self.setStyleSheet(sts)

@dataclass
class Text(Widget, QLabel):
    def __post_init__(self):
        QLabel.__init__(self)
        self.style("Text")
        
@dataclass
class Input(Widget, QLineEdit):
    def __post_init__(self):
        QLineEdit.__init__(self)
        self.style("Input")

@dataclass
class Button(Widget, QPushButton):
    def __post_init__(self):
        QPushButton.__init__(self)
        self.style("Button")

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        colorList = ['red', 'green', 'orange', 'blue']
        alineado = [
            ("hC", "vC"), 
            ("aL", "aB"),
            ("aR", "aT"),
            ("hC", "vC")
            ]
        layout = QVBoxLayout()
        for c, a in zip(colorList, alineado):
            t = f"texto #{c}"
            layout.addWidget(Text(t, "NovaMono", 20, "cyan", c, a[0], a[1]))
        layout.addWidget(Input(foreg="red", backg="yellow"))
        b = Button("Botón", "Victor Mono", 30, "red", "orange", radius=20)
        layout.addWidget(b)
        layout.addWidget(Text("pablo", "Ani", 20, "grey", "blue", "aR", "aT", radius=0))
        layout.addWidget(Text("kan", "Victor Mono", 20, "red", "orange", "aL", "aB", 3))
        
        layout.addWidget(Text("Manchester City"))
        
        layout.addWidget(Text("Liverpool", hAlign="aR"))
        layout.addWidget(Text("lo mismo", border=10))
        layout.addWidget(Input("lo mismo"))
        
        centralWidget = QWidget()
        centralWidget.setLayout(layout)
        self.setCentralWidget(centralWidget)

if __name__ == '__main__':
    app = QApplication()
    window = MainWindow()
    window.resize(500, 1000)
    window.show()
    app.exec()