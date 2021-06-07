"""
using RASPI AND ARDUINO UNO

"""

import serial
import numpy

# OPEN PORTS
#ser0=serial.Serial('/dev/ttyACM0',9600,timeout=1)
ser1=serial.Serial('/dev/ttyACM1',9600,timeout=1)
#ser2=serial.Serial('/dev/ttyACM2',9600,timeout=1)

#FIND WHICH PORT IS THE UNO
#ser0.writelines('*IDN?\n')
#print("ACM0 :" +ser0.readline().rstrip())
ser1.writelines('*IDN?\n')
print("ACM1 :" +ser1.readline().rstrip())
#ser2.writelines('*IDN?\n')
#print("ACM2 :" +ser2.readline().rstrip())

#SEND A VALUE AND SEE IF IT COMES BACK
ser1.flushInput()
ser1.writelines(':acquire1:lmemory?\n')
#for i in range(999):
    #print("trying " +str(i))
#    if (ser0.inWaiting()>0):
##        input=ser0.readline().rstrip()
#        print(input)

while ser1.inWaiting()==0:
    pass
x=ser1.readlines()

#y=numpy.fromstring(x,)
print(x)

        
# CLOSE PORTS
#ser0.close()
ser1.close()
#ser2.close()
