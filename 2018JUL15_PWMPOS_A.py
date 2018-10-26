import pigpio #HARDWARE PWM, REMEMBER TO RUN $sudo pigpiod TO START DAEMON
import sys #IMPORTS THE SYSTEM MODULE, USED FOR APPENDING PATHS FOR THE INTERPRETER
import time
sys.path.append('/home/pi/PIGPIO')
freq_PWM=9 # HZ
pi=pigpio.pi() #CREATES OBJECT FOR HARDWARE PWM
S=0.1*freq_PWM
print(S)
pi.hardware_PWM(18,freq_PWM,S)
time.sleep(10)
