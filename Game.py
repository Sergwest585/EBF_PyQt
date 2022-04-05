
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import keyboard
import time
import asyncio

import main_intf
import grid
app = QtWidgets.QApplication(sys.argv)


SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 576

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.Windows = QtWidgets.QDialog()
        self.Windows.setObjectName("Windows")
        self.Windows.setWindowModality(QtCore.Qt.WindowModal)
        self.Windows.resize(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        self.sizePolicy.setHorizontalStretch(0)
        self.sizePolicy.setVerticalStretch(0)
        self.Windows.setSizePolicy(self.sizePolicy)
        self.Windows.setWindowTitle("EBF pyqt")
        self.Windows.setWindowOpacity(1.0)
        QtCore.QMetaObject.connectSlotsByName(self.Windows)

    def keyPressEvent(self, e):
        if (e.key() == Qt.Key_W):
            wkey()
        elif (e.key() == Qt.Key_A):
            akey()
        elif (e.key() == Qt.Key_S):
            skey()
        elif (e.key() == Qt.Key_D):
            dkey()
        elif (e.key() == Qt.Key_Q):
            self.close()

class Player:
    wish = 0
    name = "debug"
    def __init__(self, win):
        self.x = [0,0,0]
        self.y = [0,0,0]
        self.payer_1lb = QtWidgets.QLabel(win)
        self.payer_1lb.setEnabled(True)
        self.payer_1lb.setGeometry(QtCore.QRect(0, 0, int(SCREEN_WIDTH/20), int(SCREEN_HEIGHT/14.8)))
        self.payer_1lb.setAcceptDrops(False)
        self.payer_1lb.setAutoFillBackground(True)
        self.payer_1lb.setInputMethodHints(QtCore.Qt.ImhNone)
        self.payer_1lb.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.payer_1lb.setLineWidth(0)
        self.payer_1lb.setPixmap(QtGui.QPixmap("intface.PNG"))
        self.payer_1lb.setScaledContents(True)
        self.payer_1lb.setObjectName("payer_lb")
        self.payer_1lb.raise_()
        self.payer_2lb = QtWidgets.QLabel(win)
        self.payer_2lb.setEnabled(True)
        self.payer_2lb.setGeometry(QtCore.QRect(0, 0, int(SCREEN_WIDTH/20), int(SCREEN_HEIGHT/14.8)))
        self.payer_2lb.setAcceptDrops(False)
        self.payer_2lb.setAutoFillBackground(True)
        self.payer_2lb.setInputMethodHints(QtCore.Qt.ImhNone)
        self.payer_2lb.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.payer_2lb.setLineWidth(0)
        self.payer_2lb.setPixmap(QtGui.QPixmap("intface.PNG"))
        self.payer_2lb.setScaledContents(True)
        self.payer_2lb.setObjectName("payer_lb")
        self.payer_2lb.raise_()
        self.payer_3lb = QtWidgets.QLabel(win)
        self.payer_3lb.setEnabled(True)
        self.payer_3lb.setGeometry(QtCore.QRect(0, 0, int(SCREEN_WIDTH/20), int(SCREEN_HEIGHT/14.8)))
        self.payer_3lb.setAcceptDrops(False)
        self.payer_3lb.setAutoFillBackground(True)
        self.payer_3lb.setInputMethodHints(QtCore.Qt.ImhNone)
        self.payer_3lb.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.payer_3lb.setLineWidth(0)
        self.payer_3lb.setPixmap(QtGui.QPixmap("intface.PNG"))
        self.payer_3lb.setScaledContents(True)
        self.payer_3lb.setObjectName("payer_lb")
        self.payer_3lb.raise_()

    def move(self, direction):
        self.x[2] = self.x[1]
        self.x[1] = self.x[0]
        self.y[2] = self.y[1]
        self.y[1] = self.y[0]
        if (direction == 0):
            self.y[0]-=1
        elif (direction == 1):
            self.x[0]+=1
        elif (direction == 2):
            self.y[0]+=1
        elif (direction == 3):
            self.x[0]-=1
        self.payer_1lb.move(self.x[0]*int(SCREEN_WIDTH/20),self.y[0]*int(SCREEN_HEIGHT/14.84))
        self.payer_2lb.move(self.x[1]*int(SCREEN_WIDTH/20),self.y[1]*int(SCREEN_HEIGHT/14.81))
        self.payer_3lb.move(self.x[2]*int(SCREEN_WIDTH/20),self.y[2]*int(SCREEN_HEIGHT/14.81))
        print(self.name, self.x[0])

    def set_cord(self, x, y):
        pass



if __name__ == "__main__":
    Window = MainWindow()
    main_ui = main_intf.Main_ui(Window, SCREEN_WIDTH, SCREEN_HEIGHT)
    grid_w = grid.Grid(Window, SCREEN_WIDTH, SCREEN_HEIGHT)
    player = Player(Window)
    player.name = "er"

    def wkey():
        player.move(0)
    def akey():
        player.move(3)
    def skey():
        player.move(2)
    def dkey():
        player.move(1)



    Window.show()
    sys.exit(app.exec_())


