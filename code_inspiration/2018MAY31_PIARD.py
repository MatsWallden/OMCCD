"""

FUNCTION:



"""

import serial

serARD=serial.Serial('/dev/ttyACM1',9600,timeout=0.5)
#serARD.readlines());
serARD.flushInput()
serARD.flushOutput()
message=1.0
print("printing to the arduino")
print(str(message))
serARD.write(str(message))

while serARD.inWaiting()==0:
    pass

data=serARD.readline()
print(data.rstrip())

##dataPlusOne=float(data)+1.0
##
##print(dataPlusOne)
##

serARD.close()
