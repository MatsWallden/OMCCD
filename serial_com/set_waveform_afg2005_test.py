"""[summary]
"""
import serial
from serial_com.get_port_sequence import get_port_sequence
from serial_com.get_serial_gwafg2005 import get_serial_gwafg2005
from serial_com.waveform_afg2005 import WaveFormAfg2005
from serial_com.is_device_gwafg2005 import is_device_gwafg2005
from serial_com.set_waveform_afg2005 import set_waveform_afg2005
THE_SERIAL=get_serial_gwafg2005(a_port_sequence=get_port_sequence())
THE_WAVEFORM=WaveFormAfg2005.SINusoid
def test_set_waveform_afg2005_00():
    """[summary]
    """
    actual=set_waveform_afg2005(a_serial=THE_SERIAL,a_waveform=THE_WAVEFORM)    

    assert actual is None
def test_set_waveform_afg2005_01():
    """[summary]
    """
    the_waveform=WaveFormAfg2005.RAMP
    actual=set_waveform_afg2005(a_serial=THE_SERIAL,a_waveform=the_waveform)    

    assert actual is None
