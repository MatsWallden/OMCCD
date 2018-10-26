"""
FUNCTION: FIND AND RETURN A PORT WITH GWGDS1072AU CONNECTED

AUTHOR: MATS WALLDEN

EMAIL: mats@wallden.eu
"""
import serial
from serialComGetPorts import serialComGetPorts
from serialComIsDeviceGWGDS1072AU import serialComIsDeviceGWGDS1072AU

def serialComGetPortGWGDS1072AU(portList):
    isAvailable=False
    #portList=serialComGetPorts()
    for i in range(len(portList)):
        obj=serial.Serial(portList[i],timeout=0.5)
        isIt=serialComIsDeviceGWGDS1072AU(obj)
        if not isIt:
            obj.close()
        else:
            print("FOUND GWGDS1072AU at " +portList[i])
            isAvailable=True
            break
            
    if isAvailable:
        return obj
    else:
        return False

    


