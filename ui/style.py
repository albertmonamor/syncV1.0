from PyQt5.Qt import *
from PyQt5.QtWidgets import *


def qLabel(text, style):
    l = QLabel(text)
    l.setStyleSheet(style)
    l.setWordWrap(True)
    return l


def QButton(text, style):
    b = QPushButton(text)
    b.setMinimumHeight(25)
    b.setStyleSheet(style)
    b.setCursor(Qt.PointingHandCursor)
    return b


Templates = {"window": "*{background:rgb(20,20,33);font-family:consolas;border-radius:7px;}",
             "label": "*{color:rgb(72,130,46);border-radius:7px;}*:hover{color:rgb(102,130,76);}",
             "select": "*{color:rgb(252,216,199);}",
             "button": "*{color:rgb(124,106,54);background:rgb(20,20,20);}"
                       "*:hover{border:1px solid rgb(89,138,67);background:rgb(10,10,10);}",
             "start": "*{background:rgb(30,30,30);color:rgb(149,113,16);border-radius:7px;}"
                      "*:hover{background:rgb(0,0,0);}"}
