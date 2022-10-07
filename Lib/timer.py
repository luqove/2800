import time

from PyQt5.QtCore import QThread, pyqtSignal


class TimerCount(QThread):
    timer_signal = pyqtSignal()

    def __init__(self, time_gap):
        super(TimerCount, self).__init__()
        self.time_gap = time_gap

    def run(self):
        while not (self.isInterruptionRequested()):
            time.sleep(self.time_gap)
            self.timer_signal.emit()
