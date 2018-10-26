"""
using RASPI AND ARDUINO UNO

"""

import serial
#import numpy
#from time import gmtime, strftime
import time # imports the time module
from struct import unpack_from
from serialComGWGDS1072AUgetPotScale import serialComGWGDS1072AUgetPotScale
from serialComGWGDS1072AUgetPotOffset import serialComGWGDS1072AUgetPotOffset


#OPEN PORTS
#ser0=serial.Serial('/dev/ttyACM0',9600,timeout=1)
ser1=serial.Serial('/dev/ttyACM1',baudrate=384000,bytesize=8,parity='N',stopbits=1,xonxoff=False,dsrdtr=False,timeout=0.5)
#ser2=serial.Serial('/dev/ttyACM2',9600,timeout=1)

#print("The time is "  + strftime("%H:%M:%S",gmtime())
#print(time.clock()) #PRINTS THE TIME

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
    ser1.writelines(':ACQ2:STAT?\n')    #QUERRY ACQUISTION STATUS CHANNEL 2
    stat=ser1.read()
    if(stat[0]=='1'):
        #print('READY STATUS!')
        break    #STOP WAITING FOR ACQUISITION STATUS

#SEND A VALUE AND SEE IF IT COMES BACK
ser1.flushInput()
ser1.writelines(':ACQ2:LMEM?\n')

while ser1.inWaiting()==0:
    pass #WAITS FOR THE DATA

x0=ser1.readlines() #READS THE MEASUREMENT AS A LIST
x1=''
for i in range(len(x0)):
    x1=x1+x0[i]  #CONCATENATES ELEMENTS


##print(len(x0))
##print(len(x1))
##print(len(x0)+len(x1))
#print(x1)

##    y0=x[0] #EXTRACTS THE MEASURED VALUE FROM THE LIST
##    y1=y0[13:len(y0)]   #REMOVES THE INITIAL CHARACTERS FROM THE DATA #FIX ME!!!
##    time_interval0=unpack_from('>f',y0,6) #UNPACKS THE BYTES ASSOCIATED WITH THE TIME INTERVAL!
##    print(time_interval0[0])
##


data_index_start=14 #
data_index_end=8014 #8014 max
data_string='x=numpy.array([' 
i=0
for data_index in range(data_index_start,data_index_end,2):
    z=unpack_from('>h',x1,data_index) #UNPACKS A SHORT INTEGER FROM THE DATA
    data_string=data_string+str(z[0]) + ','
data_string=data_string+'])'
print(data_string)
#print(z[0])
 #i+=1
#print(i) #PRINTS THE NUMBER OF LOOPS

##bla=unpack_from('<h',x1,14) #UNPACKS THE BYTES ASSOCIATED WITH THE TIME INTERVAL!
##print(bla)
#scal=serialComGWGDS1072AUgetPotScale(ser1,2) #
#print(scal)

#offs=serialComGWGDS1072AUgetPotOffset(ser1,2)
#print(offs)

#ser1.flushInput()
##ser1.writelines(':CHANNEL2:SCALE?\n')
##while ser1.inWaiting()==0:
##    pass #WAITS FOR THE DATA
##bla=ser1.readlines()
##print(bla)




##print(y0[1:13])
##data_index_start=1  #
##data_index_end=4000 #
##for data_index in range(data_index_start,data_index_end,2):
##    z=unpack_from('>h',y1,data_index) #UNPACKS A SHORT INTEGER FROM THE DATA
##    print(z[0]) 

# CLOSE PORTS
#ser0.close()
ser1.close()
#ser2.close()
