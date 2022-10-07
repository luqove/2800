
from stepper_motor import StepperMotor
from const import MS1_P, MS2_P, MS3_P, STEP_P, DIR_P
def __init__(self):

    stepper_pins = [MS1_P, MS2_P, MS3_P, STEP_P, DIR_P]
    stepper = StepperMotor(stepper_pins)

    stepper.act()

