from ctypes.wintypes import PINT
import RPi.GPIO as GPIO
import time

class IRsensor(object):
    """
    IR sensor method
    """
    def __init__(self):
        self.curent_read = 0
        self.pin = pin
        GPIO.setup(self.pin, GPIO.IN)
        
    def read_data(self):
        self.current = GPIO.Input(self.pin)