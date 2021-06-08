"""[summary]
"""
from serial_com.get_serial_gwgds1072au import get_serial_gwgds1072au
from serial_com.get_port_sequence import get_port_sequence
from serial_com.post import post

THE_PORT_SEQUENCE=get_port_sequence()
THE_SERIAL=get_serial_gwgds1072au(a_port_sequence=THE_PORT_SEQUENCE)

if THE_SERIAL is None:
    raise Exception("no serial object found")

THE_COMMAND=b'*idn?\n'

def test_post_00():
    """[test for function post]
    """
    actual = post(a_serial=THE_SERIAL,a_command=THE_COMMAND)

    assert not actual is None
    assert isinstance(actual, int)
    assert actual==6
