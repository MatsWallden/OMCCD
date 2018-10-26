"""

FUNCTION: IDENTIFIES A ARDUINO VOLUME ACTUATOR CONNECTED TO A SERIAL PORT 

AUTHOR: MATS WALLDEN

EMAIL: mats@wallden.eu

"""
import re #IMPORTS REGULAR EXPRESSIONS MODULE
from time import sleep
from serialComWaitForData import serialComWaitForData #FIX ME HARDCODED PATH

def serialComIsDeviceARDVOLACTUATOR(obj):

    closePort=False
    
    if not obj.is_open:
        obj.open() #OPENS THE SERIAL PORTS IF CLOSED
        closePort=True #DECISION BASIS CLOSE PORT BEFORE RETURN
    #print(obj.readline())
    obj.flushInput() #FLUSHES THE INPUT BUFFER
    obj.writelines('*IDN?\n')   #QUERRY THE PORT/DEVICE FOR ID NUMBER
    #sleep(1)
    #obj.write('*IDN?')   #QUERRY THE PORT/DEVICE FOR ID NUMBER
    serialComWaitForData(obj) #WAITS FOR DATA
    data=obj.readline()  #READS THE DATA
    #print(data)
    reResult=re.match('ARDVOLACTUATOR',data) #SEARCHES THE DATA FOR THE PATTERN
    isAFG2005=not not reResult#DECISION IS IT THE AARDUNO VOLUME ACTUATOR 

    if closePort:   #DECISION TO CLOSE PORT BEFORE RETURN
        obj.close()

    return isAFG2005
    
