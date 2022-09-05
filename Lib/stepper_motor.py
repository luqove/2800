import RPi.GPIO as GPIO
import time

#stepper motor

class StepperMotor(object):
    """This is the stepper motor method"""
    def __init__(self,motor_pins):
        self.motor_pins = motor_pins
        