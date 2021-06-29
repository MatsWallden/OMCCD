"""[module contains tests for get_signal_gwgds1072au]
"""
import serial
from serial_com.get_port_sequence import get_port_sequence
from serial_com.get_serial_gwgds1072au import get_serial_gwgds1072au
from serial_com.get_signal_scale_gwgds1072 import get_signal_scale_gwgds1072
from serial_com.get_signal_packed_gwgds1072au import get_signal_packed_gwgds1072au
from serial_com.get_signal_gwgds1072au import get_signal_gwgds1072au

THE_PORT_SEQUENCE=get_port_sequence()

if len(THE_PORT_SEQUENCE)==0 :
    raise Exception("no ports found")

THE_SERIAL=get_serial_gwgds1072au(a_port_sequence=THE_PORT_SEQUENCE)

if not isinstance(THE_SERIAL,serial.serialposix.Serial):
    raise Exception("gwgds1072  not found")

THE_CHANNEL_ID="1"

THE_SCALE=get_signal_scale_gwgds1072(a_serial=THE_SERIAL,a_channel_id=THE_CHANNEL_ID)

THE_SIGNAL_PACKED=get_signal_packed_gwgds1072au(a_serial=THE_SERIAL,a_channel_id=THE_CHANNEL_ID)

def test_get_signal_gwgds1072au_00():
    """[default case]
    """
    actual = get_signal_gwgds1072au(a_signal_packed=THE_SIGNAL_PACKED,a_scale=THE_SCALE)
    raise Exception(actual[0:5])
    assert isinstance(actual,list)
    assert len(actual) > 0

#TODO test if scale is None or wrong type