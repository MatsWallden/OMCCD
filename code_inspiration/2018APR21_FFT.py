import serial
ser=serial.Serial("/dev/ttyACM1",9600,timeout=0.1)
ser.writelines("*IDN?\n")
print(ser.readline())
for i in range(100):
    ser.writelines(":measure:vamplitude?\n")
    print(ser.readline())

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
