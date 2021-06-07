"""
FUNCTION: FIND AND RETURN A PORT WITH GWAFG2005 CONNECTED

AUTHOR: MATS WALLDEN

EMAIL: mats@wallden.eu
"""
import serial
from serialComGetPorts import serialComGetPorts
from serialComIsDeviceGWAFG2005 import serialComIsDeviceGWAFG2005

def serialComGetPortGWAFG2005(portList):
    isAvailable=False
    #portList=serialComGetPorts()
    for i in range(len(portList)):
        obj=serial.Serial(portList[i],timeout=0.5)
        isIt=serialComIsDeviceGWAFG2005(obj)
        if not isIt:
            obj.close()
        else:
            print("FOUND GWAFG2005 at " +portList[i])
            isAvailable=True
            break
            
    if isAvailable:
        return obj
    else:
        return False

    


