import serial

ser=serial.Serial("/dev/ttyACM1",9600,timeout=1)
print(ser.readline())
