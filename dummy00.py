import serial
#from serialComIsDeviceGWGDS1072AU import serialComIsDeviceGWGDS1072AU#FIX ME HARDCODED PATH
#from serialComWaitForData import serialComWaitForData #FIX ME HARDCODED PATH
#from serialComConfigurePort2018MAY16a import serialComConfigurePort2018MAY16a

from serialComGetPortGWGDS1072AU import serialComGetPortGWGDS1072AU

obj=serialComGetPortGWGDS1072AU()
obj.writelines('*IDN?\n')
print(obj.readline())

obj.close()
print('dummy00 after oclosing port')

