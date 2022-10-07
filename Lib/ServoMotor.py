import RPi.GPIO as GPIO
import time
import pigpio


class ServoMotor(object):
    """This is the servo motor for both 
        gripping and horizontal """
    
    def __init__(self, servo_pin):
        self.servo_pin = servo_pin
        self.pwm = pigpio.pi()
        self.pwm.set_mode(self.servo_pin, pigpio.OUTPUT)
        self.pwm.set_PWM_frequency(self.servo_pin, 50)
        self.act(90)
        
    def act(self, angle):
        # servo motor rotation angle
        if angle < 0:
            angle = 0
        if angle > 180:
            angle = 180
        
        # determine the PWM for a given angle
        pulse_width = ((angle*100)/9)+500
        
        # set the pulse width
        self.pwm.set_servo_pulsewidth(self.servo_pin, pulse_width)
        time.sleep(1)
        
        #turn off PWM 
        self.pwm.set_servo_pulsewidth(self.servo_pin, 0)

    def act_continues(self, angle1, angle2):
        delta_angle = (angle2 - angle1)/100
        for i in range(100):
            angle1 = angle1 + delta_angle
            self.act(angle1)
            time.sleep(0.01)

