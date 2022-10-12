import RPi.GPIO as GPIO
from gpiozero import RotaryEncoder
from gpiozero.tools import scaled_half

rotor = RotaryEncoder(21, 20)
led = PWMLED(5)
led.source = scaled_half(rotor.values)