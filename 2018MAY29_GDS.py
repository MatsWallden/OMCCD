"""
FUNCTION: TESTS FOR OMCD VOLUME CONTROL

"""

import serial
import numpy
#from time import gmtime, strftime
import time # imports the time module
from struct import unpack_from
from serialComWaitForData import serialComWaitForData
from serialComGWGDS1072AUgetPotScale import serialComGWGDS1072AUgetPotScale
from serialComGWGDS1072AUgetPotOffset import serialComGWGDS1072AUgetPotOffset
from serialComGetPortGWGDS1072AU import serialComGetPortGWGDS1072AU
from serialComGetPortGWAFG2005 import serialComGetPortGWAFG2005
from serialComConfigurePort2018MAY16a import serialComConfigurePort2018MAY16a
from serialComWaitForGWGDS1072AcqStatus import serialComWaitForGWGDS1072AcqStatus
from serialComIsDeviceARDVOLACTUATOR import serialComIsDeviceARDVOLACTUATOR
from serialComGetPortARDVOLACTUATOR import serialComGetPortARDVOLACTUATOR
from serialComGetPorts import serialComGetPorts

freq_excite=1.0e5 #EXCITATION FREQUENCY [Hz] #FIX ME! SET AND READ FROM THE AFG
#OPEN PORTS
portList=serialComGetPorts()
serGDS=serialComGetPortGWGDS1072AU(portList) #OPENS A PORT  TO A GDS 1072AU DEVICE IF AVAILABLE
serialComConfigurePort2018MAY16a(serGDS) #CONFIGURES THE PORT

del portList[portList.index(serGDS.port)] #REMOVES THE OPENED PORT FROM THE LIST

serAFG=serialComGetPortGWAFG2005(portList)#CHECK ME!! DOES THE PORTS FOR THE GDS WORK AFTER THIS

del portList[portList.index(serAFG.port)] #REMOVES THE OPENED PORT FROM THE LIST

#serARD=serial.Serial(portList[0],9600,timeout=0.5)
#print("INPUT HERE")
#bla=input("WRITE 2 START")
#serARD.write("START")

serGDS.flushInput()

#PARAMETERS
ch=2 #SELECT CHANNEL ON THE GDS 1072AU USING THIS VARIABLE
potentialScale=2.0e-04 #THE POTENTIAL SCALE FOR THE GDS IN VOLTS
potentialOffset=0.0 #THE OFFSET IN VOLTS
probe=0 #THE PROBE  ATTENUATION 0=1x,1=10X
probeType=0 #THE PROBE TYPE 0=VOLTAGE,1=CURRENT
probeRatio=0.1 #THE PROBE RATIO 0.1,0.2,0.5,1,2,5,10,20,50,100,200,500,1000,20000

#serGDS.writelines(':CHANnel1:DISPLAY 0\n') #TURNS DISPLAY OFF FOR CHANNEL 1
#serGDS.writelines(':CHANnel2:DISPLAY 1\n') #TURNS DISPLAY ON FOR CHANNEL 2
#serGDS.writelines(':CHANnel2:expand 0\n')    #SETS EXPAND FROM GROUND (DIDNT WORK)
#serGDS.writelines(':CHANnel2:coupling 0\n')#DIDNT WORK
#serGDS.writelines(':CHANnel2:bwlimit 0\n') #DIDNT WORK
serGDS.writelines(':CHANnel2:invert 0\n') #TURN#DIDNT WORK OFF INVERT FOR CHANNEL
serGDS.writelines(':CHANnel2:MATH 0\n') #TURNS MATH OPTION OFF FOR CHANNEL
serGDS.writelines(':CHANnel2:Probe 0\n') # SETS THE PROBE ATTENTUATION 0=1x, 1=10x (DIDNT WORK)
serGDS.writelines(':CHANnel2:Probe:Type '+str(probeType)+'\n') # SETS THE PROBE ATTENTUATION 0=1x, 1=10x
serGDS.writelines(':CHANnel2:Probe:ratio 0.1\n') # SETS THE PROBE ATTENUATION FACTOR
serGDS.writelines(':CHANnel2:SCALe '+str(potentialScale)+'\n') # SETS THE VERTICAL SCALE
serGDS.writelines(':CHANnel2:offset '+str(potentialOffset)+'\n') #SETS THE OFFSET 

serialComWaitForGWGDS1072AcqStatus(serGDS,ch) # WAIT S FOR DEVICE TO BE READY TO ACQUIRE
data=numpy.zeros(4000) #CONTAINER FOR DATA
data_index_start=14 #
data_index_end=8014 #8014 max
n=numpy.arange(0.0,len(data)) #INDEX FOR UNPACKED FORMATTED DATA
omega_excite=2*numpy.pi*freq_excite #ANGULAR VEOLCITY OF THE EXCITATION 


while True:
    ##SEND A VALUE AND SEE IF IT COMES BACK
    #serGDS.flushInput()
    serGDS.writelines(':ACQ'+str(ch)+':LMEM?\n')

    while serGDS.inWaiting()==0:
        pass #WAITS FOR THE DATA

    x0=serGDS.readlines() #READS THE MEASUREMENT AS A IST
    x1=''
    for i in range(len(x0)):
        x1=x1+x0[i]  #CONCATENATES ELEMENTS


    time_interval0=unpack_from('>f',x1,6) #UNPACKS THE BYTES ASSOCIATED WITH THE TIME INTERVAL!
    time_interval=time_interval0[0]#EXTRACTS THE TIME INTERVAL

    
 
    index_data=0 #INDEX FOR UNPACKED AND FORMATTED DATA
    for data_index in range(data_index_start,data_index_end,2):
        z=unpack_from('>h',x1,data_index) #UNPACKS A SHORT INTEGER FROM THE DATA
        z1=float(z[0])#EXTRACTS THE INTEGER AND CONVERTS TO A FLOAT
        data[index_data]=(z1/127.0)*(5*potentialScale) #PROBERATIO AND SETTING ON THE TIPS!!!
        index_data+=1
 
    H_excite=numpy.sum(numpy.multiply(data,numpy.exp(-1j*omega_excite*n*time_interval)))#FREQUENCY RESPONSE AT THE EXCITATION FREQUENCY
    #print(abs(H_excite))
    S=abs(H_excite)**2/time_interval #MAGNITUDE ACCORDING TO PARSEVALS THEOREM
    print(S)

#scal=serialComGWGDS1072AUgetPotScale(serGDS,2) #GET THE POTENTIAL SCALE
#print(scal)

#offs=serialComGWGDS1072AUgetPotOffset(serGDS,2)
#print(offs)





# CLOSE PORTS
serGDS.close()
#serARD.close()
serAFG.close()
