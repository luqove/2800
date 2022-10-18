from gpiozero import Servo
from time import sleep

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
myGPIO = 12
servo = Servo(myGPIO)
x= -1
diretion = 1
while(1):
    print(x)
    x += diretion*0.01
    if x>=0.9:
        diretion = -1

    elif x<=-0.9:
        diretion = 1
    
    servo.value = x
    sleep(0.05)