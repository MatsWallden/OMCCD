"""[summary]
"""

import serial
from serial_com.get_port_sequence import get_port_sequence
from serial_com.get_serial_gwgds1072au import get_serial_gwgds1072au
from serial_com.get_signal_scale_gwgds1072 import get_signal_scale_gwgds1072
THE_CHANNEL_ID="1"
THE_PORT_SEQUENCE=get_port_sequence()

if len(THE_PORT_SEQUENCE) == 0:
    raise Exception("no ports found")

THE_SERIAL=get_serial_gwgds1072au(a_port_sequence=THE_PORT_SEQUENCE)

if not isinstance(THE_SERIAL,serial.serialposix.Serial):
    raise Exception("no gwds1072 ")

def test_get_signal_scale_gwgds1072_00():
    """[default case]
    """
    actual = get_signal_scale_gwgds1072(a_serial=THE_SERIAL,a_channel_id=THE_CHANNEL_ID)
    
    assert isinstance(actual,float)


def test_get_signal_scale_gwgds1072_01():
    """[serial is None]
    """
    the_serial=None
    actual = get_signal_scale_gwgds1072(a_serial=the_serial,a_channel_id=THE_CHANNEL_ID)
    assert actual is None

def test_get_signal_scale_gwgds1072_02():
    """[the_channel is None]
    """
    the_channel_id=None
    actual = get_signal_scale_gwgds1072(a_serial=THE_SERIAL,a_channel_id=the_channel_id)
    assert actual is None

def test_get_signal_scale_gwgds1072_03():
    """[the_channel is correct type but unfeasible]
    """
    the_channel_id="32"
    actual = get_signal_scale_gwgds1072(a_serial=THE_SERIAL,a_channel_id=the_channel_id)
    assert actual is None

def test_get_signal_scale_gwgds1072_04():
    """[the_channel is incorrect type but not None]
    """
    the_channel_id=32
    actual = get_signal_scale_gwgds1072(a_serial=THE_SERIAL,a_channel_id=the_channel_id)
    
    assert actual is None
