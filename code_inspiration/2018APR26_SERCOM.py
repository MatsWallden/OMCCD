import serial
import numpy
def repeatReadline(obj,nMax):
    cond=True
    n=0
    while cond:
        line=obj.readline()
        n+=1
        if line or n>=nMax:
            cond=False
    if n>1:
        print("tried to read reply #"+str(n))
    return line    


nMax=10
x=""
ser=serial.Serial("/dev/ttyACM1",9600,timeout=0.1)
ser.writelines("*IDN?\n")
print("Hello My names is " + repeatReadline(ser,nMax).rstrip())



#SET UP CONDITIONS
#ser.writelines(":measure:source:measure:pwidth?\n")
ser.writelines(":acquire:mode 2\n")
ser.writelines(":acquire:mode?\n")
print(":acquire mode is now set to " + repeatReadline(ser,nMax).rstrip())

ser.writelines(":acquire:average 4\n") #
ser.writelines(":acquire:average?\n")
print(":acquire average is now set to " + repeatReadline(ser,nMax).rstrip())

ser.writelines(":channel1:bwlimit 0\n")
ser.writelines(":channel1:bwlimit?\n")
print(":channel1:bwlimit is now set to " + repeatReadline(ser,nMax).rstrip())

ser.writelines(":channel1:coupling 1\n")
ser.writelines(":channel1:coupling?\n")
print(":channel1:coupling is now set to " + repeatReadline(ser,nMax).rstrip())

ser.writelines(":channel1:invert 0\n")
ser.writelines(":channel1:invert?\n")
print(":channel1:invert is now set to " + repeatReadline(ser,nMax).rstrip())

ser.writelines(":channel1:display 1\n")
ser.writelines(":channel1:display?\n")
print(":channel1:display is now set to " + repeatReadline(ser,nMax).rstrip())

ser.writelines(":channel1:math 0\n") # Sets the MATH operation
ser.writelines(":channel1:math?\n")
print(":channel1:math is now set to " + repeatReadline(ser,nMax).rstrip())

ser.writelines(":channel1:expand 0\n")
ser.writelines(":channel1:expand?\n")
print(":channel1:expand is now set to " + repeatReadline(ser,nMax).rstrip())


ser.writelines(":channel1:probe:type 0\n")
ser.writelines(":channel1:probe:type?\n")
print(":channel1:probe:type is now set to " + repeatReadline(ser,nMax).rstrip())


ser.writelines(":channel1:probe:ratio 10\n") #Set the probe ratio for attenuation
ser.writelines(":channel1:probe:ratio?\n")
print(":channel1:probe:ratio is now set to " + repeatReadline(ser,nMax).rstrip())

ser.writelines(":channel1:scale 5.000e-03\n")
ser.writelines(":channel1:scale?\n")
print(":channel1:scale is now set to " + repeatReadline(ser,nMax).rstrip())

ser.writelines(":channel1:offset 2.110e-01\n")
ser.writelines(":channel1:offset?\n")
print(":channel1:offset is now set to " + repeatReadline(ser,nMax).rstrip())

ser.writelines(":measure:source 1\n")
ser.writelines(":measure:source?\n")
print(":measure:source is now set to " + repeatReadline(ser,nMax).rstrip())

for i in range(4):
    ser.writelines(":measure:vamplitude?\n")
    x=repeatReadline(ser,nMax).rstrip()
    y=float(x)
    print(y)


#print("THE VALUE  " + repeatReadline(ser,nMax).rstrip())

#ser.writelines("*lrn?\n")
#print(float(ser.readline()))
#for i in range(99):
#ser.writelines(":measure:vamplitude?\n")
#print(float("3.590E-02\n"))
#print(s)
    #y=float(s)
    #x[0]=float(ser.readline())
#print(x.mean())


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
