"""[summary]
"""
from serial_com.get_port_sequence import get_port_sequence
from serial_com.is_any_device_gwgds1072au import is_any_device_gwgds1072au
THE_PORT_SEQUENCE=get_port_sequence()

def test_is_any_device_gwgds1072au_00():
    """[summary]
    """
    actual=is_any_device_gwgds1072au(a_port_sequence=THE_PORT_SEQUENCE)
    assert not actual is None