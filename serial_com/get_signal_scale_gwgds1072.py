"""[summary]
"""
import serial
from serial_com.is_device_gwgds1072au import is_device_gwgds1072au
from serial_com.post import post
from serial_com.wait_for_data import wait_for_data
def get_signal_scale_gwgds1072(a_serial: serial.serialposix.Serial,a_channel_id : str)->float:
    """[returns the signal scale from the oscilloscope (GDS1072)]

    Args:
        a_serial (serial.serialposix.Serial): [a serial object oscilloscope]
        a_channel_id (str): [the channel ID]
    """

    the_return=None
    the_serial=a_serial
    the_channel_id=a_channel_id

    if isinstance(the_serial,serial.serialposix.Serial) and \
        isinstance(the_channel_id,str) and \
        the_channel_id in ("1","2") and\
        is_device_gwgds1072au(obj=the_serial):

        the_command=bytes(":CHAN"+the_channel_id+":SCAL?\n","utf-8")

        post(a_serial=the_serial, a_command=the_command)
        wait_for_data(obj=the_serial,iter_max=1000)

        the_reply=the_serial.readline()

        if isinstance(the_reply,bytes):
            the_return=float(the_reply.decode("utf-8"))
        else:
            pass

    else:
        pass

    return the_return
