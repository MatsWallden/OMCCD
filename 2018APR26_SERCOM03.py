import serial
#import numpy
import re       #regexp

# FUNCTIONS
def repeatReadline(obj,nMax):
    #THIS FUNCTION REPEATS READING UNTIL IT 
    cond=True
    n=0
    while cond:
        line=obj.readline()
        n+=1
        if line or n>=nMax:
            cond=False
    if n>=nMax:
        print("tried to read reply #"+str(n))
    return line    

#PARAMETERS
rePatternGDSValue="\d{1}\.{1}\d{2,3}"#\.{1}\d{2,3}E-|+\d{2}"
nMax=10
x=""
#OPEN SERIAL PORTS
serGDS1072=serial.Serial("/dev/ttyACM1",9600,timeout=0.1)
serUno=serial.Serial("/dev/ttyACM0",9600,timeout=0.1)

print("my uno says" +serUno.readline().rstrip())
serGDS1072.writelines("*IDN?\n")
print("Hello My names is " + repeatReadline(serGDS1072,nMax).rstrip())



#SET UP CONDITIONS
#serGDS1072.writelines(":measure:source:measure:pwidth?\n")
#serGDS1072.writelines("*RST\n") #RESETS ALL CONFIGURATIONS TO DEFAULT SETTINGS
serGDS1072.writelines(":acquire:mode 2\n")
serGDS1072.writelines(":acquire:mode?\n")
print(":acquire mode is now set to " + repeatReadline(serGDS1072,nMax).rstrip())

serGDS1072.writelines(":acquire:average 4\n") #
serGDS1072.writelines(":acquire:average?\n")
print(":acquire average is now set to " + repeatReadline(serGDS1072,nMax).rstrip())

serGDS1072.writelines(":channel1:bwlimit 0\n")
serGDS1072.writelines(":channel1:bwlimit?\n")
print(":channel1:bwlimit is now set to " + repeatReadline(serGDS1072,nMax).rstrip())

serGDS1072.writelines(":channel1:coupling 1\n")
serGDS1072.writelines(":channel1:coupling?\n")
print(":channel1:coupling is now set to " + repeatReadline(serGDS1072,nMax).rstrip())

serGDS1072.writelines(":channel1:invert 0\n")
serGDS1072.writelines(":channel1:invert?\n")
print(":channel1:invert is now set to " + repeatReadline(serGDS1072,nMax).rstrip())

serGDS1072.writelines(":channel1:display 1\n")
serGDS1072.writelines(":channel1:display?\n")
print(":channel1:display is now set to " + repeatReadline(serGDS1072,nMax).rstrip())

serGDS1072.writelines(":channel1:math 0\n") # Sets the MATH operation
serGDS1072.writelines(":channel1:math?\n")
print(":channel1:math is now set to " + repeatReadline(serGDS1072,nMax).rstrip())

serGDS1072.writelines(":channel1:expand 0\n")
serGDS1072.writelines(":channel1:expand?\n")
print(":channel1:expand is now set to " + repeatReadline(serGDS1072,nMax).rstrip())


serGDS1072.writelines(":channel1:probe:type 0\n")
serGDS1072.writelines(":channel1:probe:type?\n")
print(":channel1:probe:type is now set to " + repeatReadline(serGDS1072,nMax).rstrip())


serGDS1072.writelines(":channel1:probe:ratio 10\n") #Set the probe ratio for attenuation
serGDS1072.writelines(":channel1:probe:ratio?\n")
print(":channel1:probe:ratio is now set to " + repeatReadline(serGDS1072,nMax).rstrip())

serGDS1072.writelines(":channel1:scale 5.000e-03\n")
serGDS1072.writelines(":channel1:scale?\n")
print(":channel1:scale is now set to " + repeatReadline(serGDS1072,nMax).rstrip())

serGDS1072.writelines(":channel1:offset 2.110e-01\n")
serGDS1072.writelines(":channel1:offset?\n")
print(":channel1:offset is now set to " + repeatReadline(serGDS1072,nMax).rstrip())

serGDS1072.writelines(":measure:source 1\n")
serGDS1072.writelines(":measure:source?\n")
print(":measure:source is now set to " + repeatReadline(serGDS1072,nMax).rstrip())

while True:
        serGDS1072.writelines(":measure:vamplitude?\n")
        x=repeatReadline(serGDS1072,nMax).rstrip()
        y=re.search(rePatternGDSValue,x)
        if y:
            z=int(float(x)*1000)
            serUno.write(str(z))
            print("writing the Uno " +str(z) )
        print(serUno.readline())


#print("THE VALUE  " + repeatReadline(serGDS1072,nMax).rstrip())

#serGDS1072.writelines("*lrn?\n")
#print(float(serGDS1072.readline()))
#for i in range(99):
#serGDS1072.writelines(":measure:vamplitude?\n")
#print(float("3.590E-02\n"))
#print(s)
    #y=float(s)
    #x[0]=float(serGDS1072.readline())
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
serGDS1072.close()
serUno.close()
