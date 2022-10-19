from gpiozero import Servo
from time import sleep
import RPi.GPIO as GPIO

class ServoMotor(object):
    
    Forward = 1
    Backward = -1
    
    def __init__(self, pin):
        self.pin = pin
        self.servo = Servo(self.pin)
        self.direction = self.Forward
    
    def open_servo(self):
        self.servo.value = 1
        
    def close_servo(self):
        self.servo.value = 0