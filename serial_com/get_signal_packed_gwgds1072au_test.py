"""[summary]
"""
import serial
from serial_com.get_port_sequence import get_port_sequence
from serial_com.get_serial_gwgds1072au import get_serial_gwgds1072au
from serial_com.get_signal_packed_gwgds1072au import get_signal_packed_gwgds1072au

THE_PORT_SEQUENCE=get_port_sequence()

if len(THE_PORT_SEQUENCE) == 0 :
    raise Exception("no port found")

THE_SERIAL=get_serial_gwgds1072au(a_port_sequence=THE_PORT_SEQUENCE)

if not isinstance(THE_SERIAL,serial.serialposix.Serial):
    raise Exception("no serial for gwgds1072au")

THE_CHANNEL_ID="1"

def test_get_signal_packed_gwgds1072au_00():
    """[default case]
    """
    actual = get_signal_packed_gwgds1072au(a_serial=THE_SERIAL,a_channel_id =THE_CHANNEL_ID)

    assert isinstance(actual, bytes)
    assert len(actual)==8014
#TODO do more tests
