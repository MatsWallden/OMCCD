"""
FUNCTION: FIND AND RETURN A PORT WITH GWafg2005 CONNECTED

AUTHOR: MATS WALLDEN

EMAIL: mats@wallden.eu
"""
import serial
from serial_com.is_device_gwafg2005 import is_device_gwafg2005

def get_serial_gwafg2005(a_port_sequence : list) -> serial.serialposix.Serial:
    """[summary]

    Args:
        a_port_sequence (list): [description]

    Returns:
        serial.serialposix.Serial: [description]
    """
    the_port_sequence=a_port_sequence

    if isinstance(the_port_sequence,list):
        for the_port in the_port_sequence:
            the_serial=serial.Serial(port=the_port, timeout=0.1)
            if is_device_gwafg2005(obj=the_serial):
                return the_serial

    return None
