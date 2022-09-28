import RPi.GPIO as GPIO
import time
import pigpio

#stepper motor

class StepperMotor(object):
    """This is the stepper motor method"""
    def __init__(self,motor_pin):
        self.motor_pin = motor_pin
        self.pwm = pigpio.pi()
        self.pwm.set_mode(self.motor_pin,pigpio.OUTPUT)
        self.pwm.set_PWM_frequency(100) # frequency = 100 Hz
        