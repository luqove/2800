import RPi.GPIO as GPIO
from gpiozero import RotaryEncoder
from gpiozero.tools import scaled_half

#class RotaryEncoder(object):
#    def __init__(self):

if __name__ == '__main__':
    rotor = RotaryEncoder(21, 20)
    led = PWMLED(5)
    led.source = scaled_half(rotor.values) 