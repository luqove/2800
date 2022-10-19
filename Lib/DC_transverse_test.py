import DcMotor
from time import sleep
import RPi.GPIO as GPIO

DcMotor_transverse = DcMotor(pin_in1, pin_in2, pin_pwm=None, encoder=None)
DcMotor_transverse.turn_forward()
sleep(1)
DcMotor_transverse.turn_backward()


