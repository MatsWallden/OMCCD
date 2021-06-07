"""

CAN I SEND A VALUE BY PWM FROM THE PI TO THE ARDUINO?

"""

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM) # WHAT DOES BCM STAND FOR?
GPIO.setup(13,GPIO.OUT) #PIN 25

p=GPIO.PWM(13,1000) # 50 Hz
time.sleep(10)

p.start(50)

time.sleep(10)

p.ChangeDutyCycle(10)

time.sleep(10)

p.ChangeDutyCycle(99.999)

time.sleep(10)

p.stop()

GPIO.cleanup()

