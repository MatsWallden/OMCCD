"""[summary]
"""
import serial
from serial_com.get_port_sequence import get_port_sequence
from serial_com.get_serial_gwafg2005 import get_serial_gwafg2005

THE_PORT_SEQUENCE=get_port_sequence()

def test_get_serial_gwafg2005_00():
    """[summary]
    """
    actual=get_serial_gwafg2005(a_port_sequence=THE_PORT_SEQUENCE)
    assert isinstance(actual,serial.serialposix.Serial)
    assert actual.is_open

def test_get_serial_gwafg2005_01():
    """[summary]
    """
    actual=get_serial_gwafg2005(a_port_sequence=None)
    assert actual is None
