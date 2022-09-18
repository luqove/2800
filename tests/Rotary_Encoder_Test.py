#From https://github.com/modmypi/Rotary-Encoder/blob/master/rotary_encoder.py
#Reference https://thepihut.com/blogs/raspberry-pi-tutorials/how-to-use-a-rotary-encoder-with-the-raspberry-pi
from RPi import GPIO
from time import sleep

clk = 17
dt = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(clk, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(dt, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

counter = 0
clkLastState = GPIO.input(clk)

try:
    while True:
            clkState = GPIO.input(clk)
            dtState = GPIO.input(dt)
            if clkState != clkLastState:
                    if dtState != clkState:
                        counter += 1
                    else:
                        counter -= 1
                    
                    print(counter)
            clkLastState = clkState
            sleep(0.01)
finally:
    GPIO.cleanup()