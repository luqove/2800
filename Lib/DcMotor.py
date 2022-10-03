import RPi.GPIO as GPIO
import pigpio
import time

# Dcencoder_rotate = DCEncoder(pin1)
# Dc_rotate = DcMotorDriver(1,2,3, Dcencoder_rotate)
from PyQt5.QtCore import QThread, pyqtSignal


class DcMotor(QThread):
    # 用于向父线程反馈Encoder的数值。
    encode_value = pyqtSignal(int)

    def __init__(self, pin_in1, pin_in2, pin_pwm, encoder=None):
        super(DcMotor, self).__init__()
        self.pin_in1 = pin_in1
        self.pin_in2 = pin_in2
        self.pin_pwm = pin_pwm
        self.encoder = encoder

        GPIO.setup(self.pin_in1, GPIO.OUT)
        GPIO.setup(self.pin_in2, GPIO.OUT)

        # Pigpio generates a PWM signal from the built in hardware of the RasPi
        self.pwm = pigpio.pi()
        self.pwm.set_mode(self.pin_pwm, pigpio.OUTPUT)
        # TODO 具体如何输出pwm信号要再看看
        # self.pwm.set_PWM_frequency(self.servo_pin, 50) # 50 Hz
        # self.act(90)

        # initial motor pins
        for outpin in self.motor_pins:
            GPIO.setup(outpin, GPIO.OUT)
            GPIO.output(outpin, 0)

    def turn_forward(self):
        # 正转
        GPIO.output(self.pin_in1, 1)
        GPIO.output(self.pin_in2, 0)
        # TODO 可能使用PWM信号控制速度

    def turn_backward(self):
        GPIO.output(self.pin_in1, 0)
        GPIO.output(self.pin_in2, 1)
        # TODO 可能使用PWM信号控制速度

    def send_encoder_value(self):
        # 向父线程反馈Encoder的数值。
        self.encode_value.emit(self.encoder.value)

    def turn_off(self):
        GPIO.output(self.pin_in1, 0)
        GPIO.output(self.pin_in2, 0)

    def set_pwm(self):
        # TODO 用于设定pwm
        pass
