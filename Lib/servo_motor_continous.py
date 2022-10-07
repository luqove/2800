import RPi.GPIO as GPIO
import pigpio
import time
from servo_motor import ServoMotor_gripper
from Lib.const import *


class ServoMotor_continous(ServoMotor_gripper):
    
    def __init__(self,pwm_pin):
        super(ServoMotor_continous, self).__init__()
        self.pwm_pin = ServoMotor_gripper()
        
        
    def rotate(self):
        self.pwm_pin.set_servo_pulsewidth(servo_pin_continous,2500)
        self.pwm_pin.set_PWM_dutycycle(servo_pin_continous,255)
        
    def back_rotate(self):
        self.pwm_pin.set_PWM_dutycycle(servo_pin_continous,1500)
        self.pwm_pin.act()
        
        
