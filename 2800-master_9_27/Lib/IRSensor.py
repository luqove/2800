import RPi.GPIO as GPIO


class IRsensor(object):
    """
    IR sensor method
    """

    def __init__(self, pin):
        self.pin = pin
        GPIO.setup(self.pin, GPIO.IN)

    def read_data(self):
        return GPIO.Input(self.pin)
