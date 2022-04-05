from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
import Game
from functools import partial

class Grid(object):
    def __init__(self, Dialog, win_w, win_h):
        self.bg = QtWidgets.QLabel(Dialog)
        self.bg.setEnabled(True)
        self.bg.setGeometry(QtCore.QRect(0, 0, win_w, win_h-int(win_w/10)))
        self.bg.setAcceptDrops(False)
        self.bg.setAutoFillBackground(True)
        self.bg.setInputMethodHints(QtCore.Qt.ImhNone)
        self.bg.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.bg.setLineWidth(0)
        self.bg.setPixmap(QtGui.QPixmap("loc1_bg.png"))
        self.bg.setScaledContents(True)
        self.bg.setObjectName("bg")
        for i in range(20):
            for j in range(12):
                self.grid_b = QtWidgets.QPushButton(Dialog)
                self.grid_b.setGeometry(QtCore.QRect(int(win_w/20*i), int(win_h/14.8*j), int(win_w/20), int(win_h/14.8)))
                self.grid_b.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.grid_b.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"color: rgba(255, 255, 255, 0);")
                self.opacity_effect = QGraphicsOpacityEffect()
                self.opacity_effect.setOpacity(0.3)
                self.grid_b.setGraphicsEffect(self.opacity_effect)
                self.grid_b.setObjectName("grid_b")
                self.x = i
                self.y = j
                #self.grid_b.clicked.connect(partial(Game.move_to,self.x,self.y, self.grid_b))




