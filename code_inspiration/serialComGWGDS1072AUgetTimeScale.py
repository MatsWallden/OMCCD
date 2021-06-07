"""

FUNCTION: RETRIEVES THE SCALE FOR THE POTENTIAL OF THE GDS 1072AU
AUTHOR: MATS WALLDEN
EMAIL: mats@wallden.eu

"""
from serialComWaitForData import serialComWaitForData 
def serialComGWGDS1072AUgetTimeScale(obj):
    obj.flushInput() # FLUSHES THE INPUT
    obj.writelines(':TIMebase:SCALe?\n') #QUERRY THE GDS FOR THE SCALE
    serialComWaitForData(obj) #WAITS FOR A REPLY FROM THE GDS
    scale=obj.readline().rstrip() #READ THE QUERRY AND STRIPS TRAILING NEWLINE
    #print(scale)
    return scale
