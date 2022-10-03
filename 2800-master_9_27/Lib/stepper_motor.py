# import RPi.GPIO as GPIO
import pigpio as GPIO
import time

# 反转半圈
half_seq_ccw = [[1, 0, 0, 0],
                [1, 1, 0, 0],
                [0, 1, 0, 0],
                [0, 1, 1, 0],
                [0, 0, 1, 0],
                [0, 0, 1, 1],
                [0, 0, 0, 1],
                [1, 0, 0, 1]]

# 正转半圈
half_seq_cw = [[0, 0, 0, 1],
               [0, 0, 1, 1],
               [0, 0, 1, 0],
               [0, 1, 1, 0],
               [0, 1, 0, 0],
               [1, 1, 0, 0],
               [1, 0, 0, 0],
               [1, 0, 0, 1]]

# 反转一整圈
full_seq_ccw = [[1, 0, 0, 0],
                [0, 1, 0, 0],
                [0, 0, 1, 0],
                [0, 0, 0, 1]]
# 正转一整圈
full_seq_cw = [[0, 0, 0, 1],
               [0, 0, 1, 0],
               [0, 1, 0, 0],
               [1, 0, 0, 0]]


class StepperMotor(object):
    """This is the stepper motor method"""

    def __init__(self, motor_pins):
        # One motor corresponds to four pins,
        # and the following are the corresponding pins of two motors. need to be entered when creating。
        # [3, 5, 7, 11], [16, 18, 22, 24]
        self.motor_pins = motor_pins

        # initial motor pins
        for outpin in self.motor_pins:
            GPIO.setup(outpin, GPIO.OUT)
            GPIO.output(outpin, 0)

    def act(self, angle, direction):
        # The motor requires 8 cycles through a 64:1 gear ratio, to achieve a full cycle
        # Limiting the function to full cycles simplifies the code and is enough precision for the task at hand

        # Repeat loop for however many sequences requested, 512 sequences per revolution
        if direction == "cw":
            pass
        elif direction == "ccw":
            pass
        else:
            print("Incorrect direction entered.")

        # Turn off pins
        for pin in range(4):
            GPIO.output(self.motor_pins[pin], 0)


