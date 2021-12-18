"""[summary]
REQUIRES A DEVICE TO BE CONNECTED
"""
from serial_com.get_port_sequence import get_port_sequence

def test_get_port_sequence_00():
    """[summary]
    default case
    """
    actual = get_port_sequence()

    assert isinstance(actual,list)
    assert len(actual)==2
    assert '/dev/ttyACM0' in actual
    assert '/dev/ttyACM1' in actual
