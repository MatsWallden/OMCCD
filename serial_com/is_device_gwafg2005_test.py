"""[summary]
"""
from serial.serialutil import Timeout
from serial_com.get_port_sequence import get_port_sequence
from serial_com.is_device_gwafg2005 import is_device_gwafg2005
import serial
THE_PORT_SEQUENCE=get_port_sequence()

def test_is_device_gwafg2005_00():
    is_it=False
    for the_port in THE_PORT_SEQUENCE:
        if is_device_gwafg2005(obj=serial.Serial(port=the_port,timeout=0.1)):
            is_it=True
        else:
            pass
    assert is_it