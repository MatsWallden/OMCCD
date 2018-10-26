
"""

FUNCTION: WAITS FOR DATA FROM SERIAL PORT

AUTHOR: MATS WALLDEN

EMAIL:mats@wallden.eu

"""

def serialComWaitForData(obj,iterMax=1000):
    dataAvailable=False
    it=0 #INITIALIZE THE ITERATOR TO 0
    while not dataAvailable: #
        it+=1 #INCREMENTS THE ITERATOR
        if it>iterMax:
            print("EXCEEDED NUMBER OF INTERATIONS WHEN WAITING FOR DATA")
            break #BREAK DUE TO EXCEEDED ITERATIONS
        dataAvailable=obj.inWaiting()==0
        pass #WAITS FOR THE DATA
    return dataAvailable  
