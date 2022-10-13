import RPi.GPIO as GPIO
import pigpio
import time


class DcMotor(object):

    def __init__(self, pin_in1, pin_in2, pin_pwm, encoder=None):
        self.pin_in1 = pin_in1
        self.pin_in2 = pin_in2
        self.pin_pwm = pin_pwm
        self.encoder = encoder

        GPIO.setup(self.pin_in1, GPIO.OUT)
        GPIO.setup(self.pin_in2, GPIO.OUT)
        GPIO.setup(self.pin_pwm, GPIO.OUT)

        # Pigpio generates a PWM signal from the built in hardware of the RasPi
        self.pwm = pigpio.pi()
        self.pwm.set_mode(self.pin_pwm, pigpio.OUTPUT)
        self.pwm.set_PWM_frequency(self.pin_pwm, 50)  # 50 Hz

        # # initial motor pins
        # for outpin in self.motor_pins:
        #     GPIO.setup(outpin, GPIO.OUT)
        #     GPIO.output(outpin, 0)

    def turn_forward(self):
        # 正转
        GPIO.output(self.pin_in1, 1)
        GPIO.output(self.pin_in2, 0)

    def turn_backward(self):
        GPIO.output(self.pin_in1, 0)
        GPIO.output(self.pin_in2, 1)

    def turn_off(self):
        GPIO.output(self.pin_in1, 0)
        GPIO.output(self.pin_in2, 0)

    def set_pwm(self, dutycycle=255):
        self.pwm.set_PWM_dutycycle(self.pin_pwm, dutycycle)

    def pwm_on(self):
        self.set_pwm(255)

    def pwm_off(self):
        self.set_pwm(0)
