"""
FUNCTION: FIND AND RETURN A PORT WITH GWGDS1072AU CONNECTED

AUTHOR: MATS WALLDEN

EMAIL: mats@wallden.eu
"""
from serial_com.is_device_gwgds1072au import is_device_gwgds1072au
from serial_com.is_any_device_gwafg2005 import is_any_device_gwafg2005
from serial_com.is_any_device_gwgds1072au import is_any_device_gwgds1072au
import serial

def get_port_gwgds1072au(a_port_sequence : list) -> 'serial.Serial':
    """[summary]
    """  
    the_port_sequence=a_port_sequence
    the_return=None  
    if the_port_sequence is None:
        the_return=None
    else:
        if str(type(the_port_sequence))!="<class 'list'>":
            the_return = None
        else:
            if not is_any_device_gwgds1072au(a_port_sequence=the_port_sequence):
                the_return= None
            else:
                for the_port in the_port_sequence:
                    the_port=serial.Serial(port=the_port, timeout=0.1) #TODO configure
                    if(is_device_gwgds1072au(obj=the_port)):
                        the_return=the_port
                    else:
                        pass
    return the_port

