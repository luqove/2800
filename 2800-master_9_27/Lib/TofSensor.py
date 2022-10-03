import RPi.GPIO as GPIO
import time


class Tofsensor(object):
    """_summary_
    method for time of flight sensor
    """
    def __init__(self, pin):
        self.pin = pin
        GPIO.setup(pin, GPIO.IN)
        self.time = 0
        
    def read_data(self):
        self.current_read = GPIO.Input(self.pin)

