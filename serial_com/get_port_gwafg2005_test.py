"""[summary]
"""
from serial_com.get_port_sequence import get_port_sequence
from serial_com.get_port_gwafg2005 import get_port_gwafg2005
THE_PORT_SEQUENCE=get_port_sequence()
def test_get_port_gwafg2005_00():
    """[summary]
    """
    actual=get_port_gwafg2005(a_port_sequence=THE_PORT_SEQUENCE)
    assert not actual is None