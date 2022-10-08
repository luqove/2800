import sys
import time
from PyQt5.QtCore import Qt, pyqtSignal, QThread, QMutex
from PyQt5.QtWidgets import QApplication, QMainWindow
from MainPanel import Ui_MainWindow
from ConveyorSys import ConveyorSys
from Lib.timer import TimerCount
import RPi.GPIO as GPIO

mutex = QMutex()


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        # self.Start_btn.clicked.connect(self.start_conveyor_machine)
        self.Start_btn.clicked.connect(self.test)
        self.Stop_btn.clicked.connect(self.stop_conveyor_machine)
        self.Stop_btn.clicked.connect(self.stop_test)

    def start_conveyor_machine(self):
        self.conveyor_sys = ConveyorSys()
        # TODO 一些预定义和需要连接的信号
        self.conveyor_sys.start()

    def stop_conveyor_machine(self):
        if hasattr(self, 'conveyor_sys'):
            mutex.lock()
            self.conveyor_sys.requestInterruption()
            self.conveyor_sys.quit()
            mutex.unlock()
            del self.conveyor_sys

    def test(self):
        self.timer = TimerCount(1)
        self.timer.timer_signal.connect(self.test_feedback)
        self.timer.start()

    def stop_test(self):
        if hasattr(self, 'timer'):
            mutex.lock()
            self.timer.requestInterruption()
            self.timer.quit()
            mutex.unlock()
            del self.timer

    def test_feedback(self):
        self.print_f('1')


    def print_f(self, info):
        self.Feedback_bro.append(info)


if __name__ == '__main__':
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    app = QApplication(sys.argv)
    win = MainWindow()
    print('Window Set up')
    win.show()
    print('Window Shown')
    sys.exit(app.exec_())
