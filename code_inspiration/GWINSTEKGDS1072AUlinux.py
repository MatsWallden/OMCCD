Python 2.7.13 (default, Nov 24 2017, 17:33:09) 
[GCC 6.3.0 20170516] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> import serial
>>> ser=serial.Serial("/dev/ttyACM0",9600,timeout=1.0,rtscts=1)
>>> ser.is_open
True
>>> ser.writelines("*IDN?\n")
>>> x=ser.readlines()
>>> print(x)
['GW,GDS-1072A-U,GEQ200758,V1.14\n']
>>> ser.writelines(":SINGLE\n")
>>> ser.writelines(":RUN\n")
>>> ser.writelines(":MEASure:SOURCE 1")
>>> ser.writelines(":MEASure:VHI?\n")
>>> VHI=ser.readlines()
>>> print(VHI)
['-4.000E-04\n']
>>> ser.writelines(":MEASure:Vamp?\n")
>>> VAMP=ser.readlines()
>>> print(VAMP)
['3.590E-03\n']
>>> pasdfrint 
KeyboardInterrupt
>>> #I just used my raspi 3 B and python to measure the amplitude of AC 113 kHz using my oscilloscope:)
