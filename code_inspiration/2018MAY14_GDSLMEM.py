"""
using RASPI AND ARDUINO UNO

"""

import serial
import numpy
#from time import gmtime, strftime
import time # imports the time module

#OPEN PORTS
#ser0=serial.Serial('/dev/ttyACM0',9600,timeout=1)
ser1=serial.Serial('/dev/ttyACM1',baudrate=384000,bytesize=8,parity='N',stopbits=1,xonxoff=False,dsrdtr=False,timeout=0.5)
#ser2=serial.Serial('/dev/ttyACM2',9600,timeout=1)

#print("The time is "  + strftime("%H:%M:%S",gmtime())
print(time.clock())
#FIND WHICH PORT IS THE UNO
#ser0.writelines('*IDN?\n')
#print("ACM0 :" +ser0.readline().rstrip())
ser1.flushInput()
#ser1.writelines('*IDN?\n')
#print("ACM1 :" +ser1.readline().rstrip())
#ser1.writelines('*lrn?')
#print(ser1.readlines())
#ser2.writelines('*IDN?\n')
#print("ACM2 :" +ser2.readline().rstrip())

#ACQUISITION STATUS

while True:
    ser1.writelines(':ACQ2:STAT?\n')
    stat=ser1.read()
    if(stat[0]=='1'):
        #print('READY STATUS!')
        break    


#SEND A VALUE AND SEE IF IT COMES BACK
for i in range(1):
    ser1.flushInput()
    ser1.writelines(':ACQ2:LMEM?\n')

    while ser1.inWaiting()==0:
        pass
    x=ser1.readlines()
    #print('Number of elements is: ' +str(len(x)))

    print(x)
        
# CLOSE PORTS
#ser0.close()
ser1.close()
#ser2.close()
