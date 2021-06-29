"""[summary]
"""
from serial_com.get_port_sequence import get_port_sequence
from serial_com.get_serial_gwgds1072au import get_serial_gwgds1072au
from serial_com.is_device_gwgds1072au import is_device_gwgds1072au
from serial_com.set_autoset_gwgds1072au import set_autoset_gwgds1072au
THE_SERIAL=get_serial_gwgds1072au(a_port_sequence=get_port_sequence())
def test_set_autoset_gwgds1072_00():
    """[case default]
    """
    actual=set_autoset_gwgds1072au(a_serial=THE_SERIAL)

    assert actual is None
# def test_set_autoset_gwgds1072_01():
#     """[summary]
#     """
#     the_autoset=500
#     actual=set_autoset_gwgds1072(a_serial=THE_SERIAL,a_autoset=the_autoset)    

#     assert actual is None
