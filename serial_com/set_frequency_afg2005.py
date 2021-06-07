"""[summary]
"""
import serial
from serial_com.is_device_gwafg2005 import is_device_gwafg2005
from serial_com.post import post
def set_frequency_afg2005(a_serial: serial.serialposix.Serial, a_frequency: float):
    """[summary]

    Args:
        a_serial (serial.serialposix.Serial): [description]
        the_frequency (float): [description]
    """
    the_serial=a_serial
    if the_serial is None:
        pass
    elif not isinstance(the_serial,serial.serialposix.Serial):
        pass
    elif not the_serial.is_open:
        pass
    elif not is_device_gwafg2005(obj=the_serial):
        pass
    else:
        the_frequency=a_frequency
        if the_frequency is None:
            pass
        elif not isinstance(the_frequency,float) :
            pass
        else:
            the_command=bytes("SOUR1:FREQuency "+str(the_frequency)+'\n','utf-8')
            post(a_serial=the_serial, a_command=the_command)    