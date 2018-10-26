"""

FUNCTION: IDENTIFIES A GWINSTEK GWAFG2005 FUNCTION GENERATOR CONNECTED TO A SERIAL PORT 

AUTHOR: MATS WALLDEN

EMAIL: mats@wallden.eu

"""
import re #IMPORTS REGULAR EXPRESSIONS MODULE
from serialComWaitForData import serialComWaitForData #FIX ME HARDCODED PATH

def serialComIsDeviceGWAFG2005(obj):

    closePort=False
    
    if not obj.is_open:
        obj.open() #OPENS THE SERIAL PORTS IF CLOSED
        closePort=True #DECISION BASIS CLOSE PORT BEFORE RETURN
    
    obj.flushInput() #FLUSHES THE INPUT BUFFER
    obj.writelines('*IDN?\n')   #QUERRY THE PORT/DEVICE FOR ID NUMBER
    serialComWaitForData(obj) #WAITS FOR DATA
    data=obj.readline()  #READS THE DATA
    reResult=re.match('GW INSTEK,AFG-2005',data) #SEARCHES THE DATA FOR THE PATTERN
    isAFG2005=not not reResult#DECISION IS IT THE AFG2005

    if closePort:   #DECISION TO CLOSE PORT BEFORE RETURN
        obj.close()

    return isAFG2005
    
