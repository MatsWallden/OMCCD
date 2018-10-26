"""
FUNCTION: FIND AND RETURN A PORT WITH ARDUINO UNO VOLUME ACTUATOR CONNECTED

AUTHOR: MATS WALLDEN

EMAIL: mats@wallden.eu
"""
import serial
from serialComGetPorts import serialComGetPorts
from serialComIsDeviceARDVOLACTUATOR import serialComIsDeviceARDVOLACTUATOR

def serialComGetPortARDVOLACTUATOR():
    isAvailable=False
    portList=serialComGetPorts()
    for i in range(len(portList)):
        print(portList[i])
        obj=serial.Serial(portList[i],timeout=1.0)
        isIt=serialComIsDeviceARDVOLACTUATOR(obj)
        if not isIt:
            obj.close()
        else:
            print("FOUND ARDVOLACTUATOR at " +portList[i])
            isAvailable=True
            break
            
    if isAvailable:
        return obj
    else:
        return False

    


