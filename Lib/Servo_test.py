from gpiozero import Servo
from time import sleep, time

if __name__ == '__main__':
    servo = Servo(5)
    servo.value(-1)
    time.sleep(1)
    servo.value(1)