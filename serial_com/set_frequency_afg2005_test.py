"""[summary]
"""
import serial
from serial_com.get_port_sequence import get_port_sequence
from serial_com.get_serial_gwafg2005 import get_serial_gwafg2005
from serial_com.is_device_gwafg2005 import is_device_gwafg2005
from serial_com.set_frequency_afg2005 import set_frequency_afg2005
THE_SERIAL=get_serial_gwafg2005(a_port_sequence=get_port_sequence())
THE_FREQUENCY=1000.
def test_set_frequency_afg2005_00():
    """[summary]
    """
    actual=set_frequency_afg2005(a_serial=THE_SERIAL,a_frequency=THE_FREQUENCY)    

    assert actual is None

# def test_set_frequency_afg2005_01():
#     """[summary]
#     """
#     the_frequency=500
#     actual=set_frequency_afg2005(a_serial=THE_SERIAL,a_frequency=the_frequency)    

#     assert actual is None
