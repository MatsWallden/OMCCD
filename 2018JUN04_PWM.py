"""

CAN I SEND A VALUE BY PWM FROM THE PI TO THE ARDUINO?

"""

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM) # WHAT DOES BCM STAND FOR?
GPIO.setup(19,GPIO.OUT) #PIN 25
Freq=1000.0
p=GPIO.PWM(19,Freq) # 50 Hz
time.sleep(10)
p.start(30)
for i in range(5):
    print("PHASE 0")
    p.ChangeDutyCycle(30)
    time.sleep(10)
    
    print("PHASE 1")
    p.ChangeDutyCycle(50)
    time.sleep(10)


p.stop()

GPIO.cleanup()

