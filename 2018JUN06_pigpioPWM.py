import pigpio
import time
import sys

sys.path.append('/home/pi/PIGPIO')
frequency=1000 
period=1000000.0/frequency
pigpio.start()
pigpio.hardware_PWM(18,800,250000)
time.sleep(5)
pig.pio.stop()
