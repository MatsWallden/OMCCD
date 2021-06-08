"""[summary]
"""
from serial_com.channelgwgds1072au import ChannelGwdGds1072Au
from serial_com.get_serial_gwgds1072au import get_serial_gwgds1072au
from serial_com.get_port_sequence import get_port_sequence
from serial_com.set_potential_offset_gwgds1072au import set_potential_offset_gwgds1072au
THE_SERIAL=get_serial_gwgds1072au(a_port_sequence=get_port_sequence())
THE_CHANNEL=ChannelGwdGds1072Au.CHANnel1
THE_POTENTIAL_OFFSET=0

def test_set_potential_offset_gwgds1072au_00():
    actual=set_potential_offset_gwgds1072au(a_serial=THE_SERIAL,a_channel=THE_CHANNEL,a_potential_offset=THE_POTENTIAL_OFFSET)
    assert actual is None