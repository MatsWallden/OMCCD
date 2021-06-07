#%%
from serial_com.is_any_device_gwgds1072au import is_any_device_gwgds1072au
from serial_com.is_any_device_gwafg2005 import is_any_device_gwafg2005
from serial_com.get_port_sequence import get_port_sequence
import re
from serial_com.wait_for_data import wait_for_data
from serial import serial
#from serial_com.GetPortGWGDS1072AU import GetPortGWGDS1072AU


#%%
portSequence=get_port_sequence()

print(portSequence)

obj=serial.Serial(portSequence[0],timeout=0.1)

obj.reset_input_buffer() #FLUSHES THE INPUT BUFFER
obj.reset_output_buffer()
obj.write(str.encode("*IDN?"))   #QUERRY THE PORT/DEVICE FOR ID NUMBER
obj.write(b'*idn?')
#obj.write('*IDN?'.encode('utf8'))   #QUERRY THE PORT/DEVICE FOR ID NUMBER
print(obj.name)
print(obj.is_open)
print(obj.out_waiting)
print(obj.bytesize)
wait_for_data(obj) #WAITS FOR DATA
data=obj.readline()  #READS THE DATA
print(data)
reResult=re.match('GW,GDS-1072A-U',str(data)) #SEARCHES THE DATA FOR THE PATTERN
isDevice=not not reResult#DECISION IS IT THE AFG2005

print(isDevice)  

 # %%
