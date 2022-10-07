import RPi.GPIO as GPIO
#import pigpio as GPIO
from RpiMotorLib import RpiMotorLib
import time

class StepperMotor(object):
    """This is the stepper motor method"""

    def __init__(self, driver_pins):
        # One motor corresponds to four pins,
        # and the following are the corresponding pins of two motors. need to be entered when creating
        # [3, 5, 7, 11], [16, 18, 22, 24]
        self.driver_pins = driver_pins

        # initial motor pins
        self.MS1 = self.driver_pins[0]
        self.MS2 = self.driver_pins[1]
        self.MS3 = self.driver_pins[2]
        self.GPIO_pins = (self.MS1, self.MS2, self.MS3)
        self.STEP_PWM = self.driver_pins[3]
        self.DIR = self.driver_pins[4]

        # Declare an named instance of class pass GPIO pins numbers
        self.step_motor = RpiMotorLib.A4988Nema(self.DIR, self.STEP_PWM, self.GPIO_pins, "A4988")

    def act(self, clock_wise=False, step_type="Full", steps=100, step_delay=0.01, verbose=False, init_delay=0.05):
        # call the function
        self.step_motor.motor_go(clock_wise,
                                 step_type,
                                 steps,
                                 step_delay,
                                 verbose,
                                 init_delay)

