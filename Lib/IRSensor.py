from ctypes.wintypes import PINT
import RPi.GPIO as GPIO
import time


class IRsensor(object):
    """
    IR sensor method
    """

    def __init__(self, pin):
        self.pin = pin
        GPIO.setup(self.pin, GPIO.IN)


    def read_data(self):
        return GPIO.Input(self.pin)
