import sys

import time
from PyQt5.QtCore import Qt, pyqtSignal, QThread, QMutex
from PyQt5.QtWidgets import QApplication, QMainWindow

mutex = QMutex()

class MainWindow(QMainWindow):
   
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)