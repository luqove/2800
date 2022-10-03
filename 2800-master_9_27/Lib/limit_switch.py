import RPi.GPIO as GPIO
import time

from PyQt5.QtCore import QThread, pyqtSignal


class LimitSwitch(QThread):
    SIG = pyqtSignal(int)

    def __init__(self, pin):
        super(LimitSwitch, self).__init__()
        pass

    # 发送信号
    def send_sig(self):
        self.SIG.emit()

    # run
    def run(self):
        self.send_sig()
        time.sleep(0.1)
