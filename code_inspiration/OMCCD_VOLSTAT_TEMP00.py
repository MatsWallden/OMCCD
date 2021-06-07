"""
FUNCTION: TESTS FOR OMCD VOLUME CONTROL

"""

import serial
import numpy
import time # imports the time module
import pigpio #HARDWARE PWM, REMEMBER TO RUN $sudo pigpiod TO START DAEMON
from struct import unpack_from
from serialComWaitForData import serialComWaitForData
from serialComGWGDS1072AUgetPotScale import serialComGWGDS1072AUgetPotScale
from serialComGWGDS1072AUgetPotOffset import serialComGWGDS1072AUgetPotOffset
from serialComGWGDS1072AUgetTimeScale import serialComGWGDS1072AUgetTimeScale
from serialComGetPortGWGDS1072AU import serialComGetPortGWGDS1072AU
from serialComGetPortGWAFG2005 import serialComGetPortGWAFG2005
#from serialComConfigurePort2018MAY16a import serialComConfigurePort2018MAY16a
from serialComConfigurePort2019APR28 import serialComConfigurePort2019APR28
from serialComWaitForGWGDS1072AcqStatus import serialComWaitForGWGDS1072AcqStatus
from serialComIsDeviceARDVOLACTUATOR import serialComIsDeviceARDVOLACTUATOR
from serialComGetPortARDVOLACTUATOR import serialComGetPortARDVOLACTUATOR
from serialComGetPorts import serialComGetPorts
import sys
sys.path.append('/home/pi/PIGPIO')

from scipy import signal

#fs=1000.0 #sample frequency

freq_excite=1.0e5 #EXCITATION FREQUENCY [Hz] #FIX ME! SET AND READ FROM THE AFG
#OPEN PORTS
portList=serialComGetPorts() #
serGDS=serialComGetPortGWGDS1072AU(portList) #OPENS A PORT  TO A GDS 1072AU DEVICE IF AVAILABLE
serialComConfigurePort2019APR28(serGDS) #CONFIGURES THE PORT
#serialComConfigurePort2018MAY16a(serGDS) #CONFIGURES THE PORT
del portList[portList.index(serGDS.port)] #REMOVES THE OPENED PORT FROM THE LIST

serAFG=serialComGetPortGWAFG2005(portList)#CHECK ME!! DOES THE PORTS FOR THE GDS WORK AFTER THIS

del portList[portList.index(serAFG.port)] #REMOVES THE OPENED PORT FROM THE LIST

serARD=serial.Serial(portList[0],timeout=0.05)


freq_PWM=90 # HZ
pi=pigpio.pi() #CREATES OBJECT FOR HARDWARE PWM

print("CONFIGURING THE GDS")
serGDS.flushInput()

#PARAMETERS FOR THE GDS 1072A-U
ch=2 #SELECT CHANNEL ON THE GDS 1072AU USING THIS VARIABLE
print(serialComGWGDS1072AUgetPotScale(serGDS,2))
potentialScale=float(serialComGWGDS1072AUgetPotScale(serGDS,2))

potentialOffset=0.0 #THE OFFSET IN VOLTS
probe=0 #THE PROBE  ATTENUATION 0=1x,1=10X
probeType=0 #THE PROBE TYPE 0=VOLTAGE,1=CURRENT
probeRatio='0.1' #THE PROBE RATIO 0.1,0.2,0.5,1,2,5,10,20,50,100,200,500,1000,20000

serGDS.writelines(':CHANnel2:invert 0\n') #TURN#DIDNT WORK OFF INVERT FOR CHANNEL
serGDS.writelines(':CHANnel2:MATH 0\n') #TURNS MATH OPTION OFF FOR CHANNEL
serGDS.writelines(':CHANnel2:Probe 0\n') # SETS THE PROBE ATTENTUATION 0=1x, 1=10x (DIDNT WORK)
serGDS.writelines(':CHANnel2:Probe:Type '+str(probeType)+'\n') # SETS THE PROBE ATTENTUATION 0=1x, 1=10x
serGDS.writelines(':CHANnel2:Probe:ratio '+ probeRatio +'\n') # SETS THE PROBE ATTENUATION FACTOR

serialComWaitForGWGDS1072AcqStatus(serGDS,ch) # WAIT S FOR DEVICE TO BE READY TO ACQUIRE
data=numpy.zeros(4000) #CONTAINER FOR DATA
data_index_start=14 #
data_index_end=8014 #8014 max
n=numpy.arange(0.0,len(data)) #INDEX FOR UNPACKED FORMATTED DATA
omega_excite=2*numpy.pi*freq_excite #ANGULAR VEOLCITY OF THE EXCITATION

Sexp=1.0# This is the setpoint for the signal
print("ENTERING LOOP")
while True:
    serARD.write("300.0")
    
    potentialScale=float(serialComGWGDS1072AUgetPotScale(serGDS,2))
    ##SEND A VALUE AND SEE IF IT COMES BACK
    serGDS.writelines(':ACQ'+str(ch)+':LMEM?\n') #INSTRUCTION TO THE GDS TO ACQUIRE WAVEFORM DATA

    while serGDS.inWaiting()==0:
        pass #WAITS FOR THE DATA

    x0=serGDS.readlines() #READS THE MEASUREMENT AS A LIST
    
    
    x1=''
    for i in range(len(x0)):
        x1=x1+x0[i]  #CONCATENATES ELEMENTS IN THE LIST
        

    time_interval0=unpack_from('>f',x1,6) #UNPACKS THE BYTES ASSOCIATED WITH THE TIME INTERVAL!
    time_interval=time_interval0[0]#EXTRACTS THE TIME INTERVAL
       
    index_data=0 #INDEX FOR UNPACKED AND FORMATTED DATA
    for data_index in range(data_index_start,data_index_end,2):
        try:
            z=unpack_from('>h',x1,data_index) #UNPACKS A SHORT INTEGER FROM THE DATA
        except:
            print("WHY?")
        z1=float(z[0])#EXTRACTS THE INTEGER AND CONVERTS TO A FLOAT
        data[index_data]=(z1/127.0)*(5*potentialScale) #PROBERATIO AND SETTING ON THE TIPS!!!
        index_data+=1

    
    H_excite=numpy.sum(numpy.multiply(data,numpy.exp(-1j*omega_excite*n*time_interval)))#FREQUENCY RESPONSE AT THE EXCITATION FREQUENCY
    S=abs(H_excite)*100000
        
    if S>=1000000:
        S=999999
    pi.hardware_PWM(18,freq_PWM,S)
    print(str(S/100) + " " + str(potentialScale))




# CLOSE PORTS
serGDS.close()
serAFG.close()
