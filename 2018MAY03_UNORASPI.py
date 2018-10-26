"""
using RASPI AND ARDUINO UNO

"""

import serial

# OPEN PORTS
ser0=serial.Serial('/dev/ttyACM0',9600,timeout=1)
#ser1=serial.Serial('/dev/ttyACM1',9600,timeout=1)
#ser2=serial.Serial('/dev/ttyACM2',9600,timeout=1)

#FIND WHICH PORT IS THE UNO
#ser0.writelines('*IDN?\n')
#print("ACM0 :" +ser0.readline().rstrip())
#ser1.writelines('*IDN?\n')
#print("ACM1 :" +ser1.readline().rstrip())
#ser2.writelines('*IDN?\n')
#print("ACM2 :" +ser2.readline().rstrip())

#SEND A VALUE AND SEE IF IT COMES BACK
ser0.flushInput()
ser0.write('1000\n')
#for i in range(999):
    #print("trying " +str(i))
#    if (ser0.inWaiting()>0):
##        input=ser0.readline().rstrip()
#        print(input)

while ser0.inWaiting()==0:
    pass
print(ser0.readline().rstrip())
        
#print(ser0.read())
#print(ser0.readline())

# CLOSE PORTS
ser0.close()
#ser1.close()
#ser2.close()
