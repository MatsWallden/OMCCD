"""
using RASPI AND ARDUINO UNO

"""

import serial
#import numpy
#from time import gmtime, strftime
import time # imports the time module
from struct import unpack_from
from serialComWaitForData import serialComWaitForData
from serialComGWGDS1072AUgetPotScale import serialComGWGDS1072AUgetPotScale
from serialComGWGDS1072AUgetPotOffset import serialComGWGDS1072AUgetPotOffset
from serialComGetPortGWGDS1072AU import serialComGetPortGWGDS1072AU
from serialComConfigurePort2018MAY16a import serialComConfigurePort2018MAY16a
from serialComWaitForGWGDS1072AcqStatus import serialComWaitForGWGDS1072AcqStatus

#OPEN PORTS
ser1=serialComGetPortGWGDS1072AU() #OPENS A PORT  TO A GDS 1072AU DEVICE IF AVAILABLE
serialComConfigurePort2018MAY16a(ser1) #CONFIGURES THE PORT

#print("The time is "  + strftime("%H:%M:%S",gmtime())
#print(time.clock()) #PRINTS THE TIME


ser1.flushInput()

#PARAMETERS
ch=2 #SELECT CHANNEL ON THE GDS 1072AU USING THIS VARIABLE
potentialScale=1.0e-01 #THE POTENTIAL SCALE FOR THE GDS IN VOLTS
potentialOffset=0.0 #THE OFFSET IN VOLTS
probe=0 #THE PROBE  ATTENUATION 0=1x,1=10X
probeType=0 #THE PROBE TYPE 0=VOLTAGE,1=CURRENT
probeRatio=10 #THE PROBE RATIO 0.1,0.2,0.5,1,2,5,10,20,50,100,200,500,1000,20000

#ser1.writelines(':CHANnel1:DISPLAY 0\n') #TURNS DISPLAY OFF FOR CHANNEL 1
#ser1.writelines(':CHANnel2:DISPLAY 1\n') #TURNS DISPLAY ON FOR CHANNEL 2
#ser1.writelines(':CHANnel2:expand 0\n')    #SETS EXPAND FROM GROUND (DIDNT WORK)
#ser1.writelines(':CHANnel2:coupling 0\n')#DIDNT WORK
#ser1.writelines(':CHANnel2:bwlimit 0\n') #DIDNT WORK
ser1.writelines(':CHANnel2:invert 0\n') #TURN#DIDNT WORK OFF INVERT FOR CHANNEL
ser1.writelines(':CHANnel2:MATH 0\n') #TURNS MATH OPTION OFF FOR CHANNEL
#ser1.writelines(':CHANnel2:Probe 1\n') # SETS THE PROBE ATTENTUATION 0=1x, 1=10x (DIDNT WORK)
ser1.writelines(':CHANnel2:Probe:Type '+str(probeType)+'\n') # SETS THE PROBE ATTENTUATION 0=1x, 1=10x
ser1.writelines(':CHANnel2:Probe:ratio 10\n') # SETS THE PROBE ATTENUATION FACTOR
ser1.writelines(':CHANnel2:SCALe '+str(potentialScale)+'\n') # SETS THE VERTICAL SCALE
ser1.writelines(':CHANnel2:offset '+str(potentialOffset)+'\n') #SETS THE OFFSET 

serialComWaitForGWGDS1072AcqStatus(ser1,ch) # WAIT S FOR DEVICE TO BE READY TO ACQUIRE

##SEND A VALUE AND SEE IF IT COMES BACK
ser1.flushInput()
ser1.writelines(':ACQ'+str(ch)+':LMEM?\n')

while ser1.inWaiting()==0:
    pass #WAITS FOR THE DATA

x0=ser1.readlines() #READS THE MEASUREMENT AS A IST
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

##x=ser1.readlines() #READS THE MEASUREMENT AS A LIST
###print(x)
##y0=x[0] #EXTRACTS THE MEASURED VALUE FROM THE LIST
##y1=y0[13:len(y0)]   #REMOVES THE INITIAL CHARACTERS FROM THE DATA #FIX ME!!!
##time_interval0=unpack_from('>f',y0,6) #UNPACKS THE BYTES ASSOCIATED WITH THE TIME INTERVAL!
##print(time_interval0[0])

data_string='x=numpy.array([' 
i=0
for data_index in range(data_index_start,data_index_end,2):
    z=unpack_from('>h',x1,data_index) #UNPACKS A SHORT INTEGER FROM THE DATA
    z1=float(z[0])#EXTRACTS THE INTEGER AND CONVERTS TO A FLOAT
    z2=(z1/127.0)*(5*potentialScale) #PROBERATIO AND SETTING ON THE TIPS!!!
    data_string=data_string+str(z2) + ',' #ADDS A SEPARATING COMMA
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





# CLOSE PORTS
#ser0.close()
ser1.close()
#ser2.close()
