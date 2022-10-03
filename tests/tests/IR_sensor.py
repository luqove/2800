import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BOARD)

PIN_TRIGGER = 7
PIN_ECHO = 11






class IR():
    def __init__(self,PIN_TRIGGER, PIN_ECHO) -> None:
        self.PIN_TRIGGER = PIN_TRIGGER
        self.PIN_ECHO = PIN_ECHO
        GPIO.setup(PIN_TRIGGER, GPIO.OUT)
        GPIO.setup(PIN_ECHO, GPIO.IN)

    def get_dist(self):
        GPIO.output (PIN_TRIGGER, GPIO.HIGH)
        time.sleep(0.0001)
        GPIO.output(PIN_TRIGGER, GPIO.LOW)
        while GPIO.input(PIN_ECHO) == 0:
            pulse_start_time = time.time()
        while GPIO.input(PIN_ECHO) == 1:
            pulse_end_time = time.time()

        pulse_distance = pulse_end_time - pulse_start_time

        distance = round(pulse_distance*17150, 2)

        print(distance)
