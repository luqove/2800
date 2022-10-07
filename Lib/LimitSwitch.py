import RPi.GPIO as GPIO
import time


class LimitSwitch(object):

    def __init__(self, pin):
        self.pin = pin
        GPIO.setup(self.pin, GPIO.IN)

    def get_read(self):
        return GPIO.Input(self.pin)
