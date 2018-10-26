import serial
import numpy
def repeatReadlines(obj,nMax):
    cond=True
    n=0
    while cond:
        line=obj.readlines(1)
        n+=1
        if line or n>=nMax:
            cond=False
    print(n)
    return line
    


x=""
ser=serial.Serial("/dev/ttyACM1",9600,timeout=0.1)

ser.writelines("*IDN?\n")
x=repeatReadlines(ser,10)
print(x)
"""ser.writelines("*IDN?\n")
cond=True
while cond:
    x=ser.readlines(1)
    if len(x) > 0:
        cond=False
        """

"""
#SET UP CONDITIONS
ser.writelines(":measure:source:measure:pwidth?\n")
print(ser.readline())
ser.writelines(":acquire:mode 2\n")
ser.writelines(":acquire:average 5\n")
ser.writelines(":channel1:bwlimit 0\n")
ser.writelines(":channel1:coupling 1\n")
ser.writelines(":channel1:invert 0\n")
ser.writelines(":channel1:display 1\n")
ser.writelines(":channel1:math 0\n") # Sets the MATH operation
ser.writelines(":channel1:expand 0\n")
ser.writelines(":channel1:probe:type 0\n")
ser.writelines(":channel1:probe:ratio 10\n") #Set the probe ratio for attenuation
ser.writelines(":channel1:scale 2.00e-2\n")
ser.writelines(":channel1:offset 1.624e-01\n")

cond=True
while cond:
    x=ser.readlines(1)
    if len(x) > 0:
        cond=False
print(x)

#ser.writelines("*lrn?\n")
#print(ser.readline())

#print(ser.readline())


#print(float(ser.readline()))
#for i in range(99):
#ser.writelines(":measure:vamplitude?\n")
#print(float("3.590E-02\n"))
#print(s)
    #y=float(s)
    #x[0]=float(ser.readline())
#print(x.mean())
""""

"""ser.writelines(":MATH:OPERator 3\n")# set operator to FFT (3)
#ser.writelines(":MATH:OPERator?\n")# query which operator is used? 3=FFT
ser.writelines(":MATH:FFT:SOURce 1\n")# set source to 1
ser.writelines(":MATH:FFT:WINDow 3\n")# set window to blackman (3)
ser.writelines(":MATH:FFT:HORizontal:POSition 200000\n")# set window to blackman (3)
ser.writelines(":measure:vamplitude\n")
#print(ser.readline())
#ser.flush()
"""
ser.close()
