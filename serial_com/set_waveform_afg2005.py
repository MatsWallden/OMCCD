"""[summary]
"""
import serial
from serial import serialposix
from serial_com.waveform_afg2005 import WaveFormAfg2005
from serial_com.post import post
from serial_com.is_device_gwafg2005 import is_device_gwafg2005

def set_waveform_afg2005(a_serial: serial.serialposix.Serial,a_waveform: WaveFormAfg2005)->None:
    """[summary]

    Args:
        a_waveform (WaveFormAfg2005): [description]
    """
    the_serial=a_serial
    if(the_serial is None):
        pass
    elif(not isinstance(the_serial,serial.serialposix.Serial)):
        pass
    elif(not the_serial.is_open):
        pass
    elif(not is_device_gwafg2005(obj=the_serial)):
        pass
    else:
        the_waveform=a_waveform
        if(the_waveform is None):
            pass
        elif(not isinstance(the_waveform,WaveFormAfg2005)):
            pass
        else:
            the_command=bytes("SOUR1:FUNCtion "+a_waveform.name+'\n','utf-8')
            post(a_serial=the_serial, a_command=the_command)
