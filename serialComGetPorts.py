"""
FUNCTION: FIND ALL PORTS

AUTHOR: MATS WALLDEN

EMAIL: mats@wallden.eu

"""

import re
import subprocess
def serialComGetPorts():
    portList0=subprocess.check_output(['ls','/dev/']) #GET ALL  LISTINGS  FOR /dev/
    portList1=re.findall('ttyACM\d{1,}',portList0)  #GET ALL LISTINGS FOR PATTERN OF PORTS
    portList=list()
    for i in range(len(portList1)):
        portList.append('/dev/'+portList1[i]) #APPEND /dev/ to the begining  of all ports
        #print portList[i]
    return portList


