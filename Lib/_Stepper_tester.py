
from StepperMotor import StepperMotor
from const import MS1_P, MS2_P, MS3_P, STEP_P, DIR_P
import RPi.GPIO as GPIO
import time
# step motor


def __main__():
    # setup()
    stepper_pins = [MS1_P, MS2_P, MS3_P, STEP_P, DIR_P]
    stepper = StepperMotor(stepper_pins)
    stepper.act(steps=500, step_delay=0.005)

    stepper.act(True, steps=200)

   
if __name__ == "__main__":
    __main__()