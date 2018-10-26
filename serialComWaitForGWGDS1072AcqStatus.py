"""
FUNCTION: WAITS FOR THE GDS1072AU TO BE READY FOR ACQUISITION

AUTHOR: MATS WALLDEN

EMAIL: mats@wallden.eu

"""
from serialComWaitForData import serialComWaitForData

def serialComWaitForGWGDS1072AcqStatus(obj,ch,maxIter=1000):
    it=0 #INITIALIZES ITERATOR TO 0
    obj.flushInput() #FLUSHES THE INPUT OF THE PORT
    while True:
        obj.writelines(':ACQ'+str(ch)+':STAT?\n')    #QUERRY ACQUISTION STATUS CHANNEL 2
        serialComWaitForData(obj) #WAITS FOR DATA
        stat=obj.read() #READ DATA
        it+=1
        if(stat and stat[0]=='1' or it>maxIter):
            print('READY STATUS!')
            break    #STOP WAITING FOR ACQUISITION STATUS
