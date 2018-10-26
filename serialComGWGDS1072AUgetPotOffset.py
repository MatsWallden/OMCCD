"""

FUNCTION: RETRIEVES THE OFFSET FOR THE POTENTIAL OF THE GDS 1072AU
AUTHOR: MATS WALLDEN
EMAIL: mats@wallden.eu

"""
from serialComWaitForData import serialComWaitForData 
def serialComGWGDS1072AUgetPotOffset(obj,ch):
    obj.flushInput() # FLUSHES THE INPUT
    obj.writelines(':CHANNEL' +str(ch)+':OFFset?\n') #QUERRY THE GDS FOR THE OFFSET
    serialComWaitForData(obj) #WAITS FOR A REPLY FROM THE GDS
    offset=obj.readline().rstrip() #READ THE QUERRY AND STRIPS TRAILING NEWLINE
    #print(scale)
    return offset
