from DcMotor import DcMotor
from time import sleep
import RPi.GPIO as GPIO


if __name__ == "__main__":
    GPIO.setmode(GPIO.BCM)
    testMotor = DcMotor(16, 20, 12)
    testMotor.pwm_off()
    testMotor.turn_forward()
    test_pwm = 0
    while test_pwm < 255:
        test_pwm += 5
        testMotor.set_pwm(test_pwm)
        sleep(0.5)
    testMotor.pwm_off()
