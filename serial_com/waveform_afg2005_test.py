"""[summary]
"""
from serial_com.waveform_afg2005 import WaveFormAfg2005
def test_WaveFormAfg2005_00():
    """[test function , testcase sinus]
    """    
    actual=WaveFormAfg2005.SINusoid
    assert isinstance(actual,WaveFormAfg2005)
    assert actual.name=="SINusoid"