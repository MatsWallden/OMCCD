"""[tests for class Device use with pytest]
"""
from uuid import uuid4
from serial_com.device import Device
THE_ID="12345"
THE_DEVICE=Device(a_id=THE_ID)
THE_COMMAND="ASDFE"

def test_device_init_00():

    assert not THE_DEVICE is None
    assert str(type(THE_DEVICE))=="<class 'serial_com.device.Device'>"

def test_device_get_id_00():
    assert THE_DEVICE.get_id()==THE_ID

def test_device_post_00():
    assert THE_DEVICE.post(a_command=THE_COMMAND) is None

def test_device_read_00():
    assert THE_DEVICE.read() is None
