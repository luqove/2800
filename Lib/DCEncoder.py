import RPi.GPIO as GPIO


class DCEncoder(object):
    def __init__(self,value):
        self.value = value
        pass