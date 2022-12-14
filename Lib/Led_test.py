import RPi.GPIO as GPIO


class LED(object):
    """
    LED 的类
    """
    def __init__(self, pin):
        self.pin = pin
        GPIO.setup(self.pin, GPIO.OUT)

    def turn_on(self):
        GPIO.output(self.pin, True)

    def turn_off(self):
        GPIO.output(self.pin, False)
