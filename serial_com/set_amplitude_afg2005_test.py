"""[summary]
"""
import serial
from serial_com.get_port_sequence import get_port_sequence
from serial_com.get_serial_gwafg2005 import get_serial_gwafg2005
from serial_com.is_device_gwafg2005 import is_device_gwafg2005
from serial_com.set_amplitude_afg2005 import set_amplitude_afg2005
THE_SERIAL=get_serial_gwafg2005(a_port_sequence=get_port_sequence())
THE_AMPLITUDE=1.0
def test_set_amplitude_afg2005_00():
    """[summary]
    """
    actual=set_amplitude_afg2005(a_serial=THE_SERIAL,a_amplitude=THE_AMPLITUDE)    

    assert actual is None
    assert False
# def test_set_amplitude_afg2005_01():
#     """[summary]
#     """
#     the_amplitude=500
#     actual=set_amplitude_afg2005(a_serial=THE_SERIAL,a_amplitude=the_amplitude)    

#     assert actual is None
