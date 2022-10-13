import RPi.GPIO as GPIO
from gpiozero import RotaryEncoder


class DCEncoder(object):
    def __init__(self, pin1, pin2):
        self.rotor = RotaryEncoder(pin1, pin2, wrap=True)
        self.rotor.steps = 0

    # step 会在motor往一个方向旋转的时候一直增加或者减少。
    def return_value(self):
        return self.rotor.steps
