"""[summary]
"""
import serial
from serial_com.is_device_gwgds1072au import is_device_gwgds1072au
from serial_com.post import post
def set_autoset_gwgds1072au(a_serial: serial.serialposix.Serial):
    """[summary]

    Args:
        a_serial (serial.serialposix.Serial): [description]
        the_amplitude (float): [description]
    """
    the_serial=a_serial
    if the_serial is None:
        pass
    elif not isinstance(the_serial,serial.serialposix.Serial):
        pass
    elif not the_serial.is_open:
        pass
    elif not is_device_gwgds1072au(obj=the_serial):
        pass
    else:
        the_command=bytes(":AUT\n",'utf-8')
        post(a_serial=the_serial, a_command=the_command)    