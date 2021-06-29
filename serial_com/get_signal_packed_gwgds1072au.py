"""[summary]
"""
import serial
from serial_com.is_device_gwgds1072au import is_device_gwgds1072au
from serial_com.post import post
from serial_com.wait_for_data import wait_for_data
def get_signal_packed_gwgds1072au(a_serial: serial.serialposix.Serial,a_channel_id : str)->bytes:
    """[returns the packed signal from the oscilloscope (GDS1072)]

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
  
        the_command=bytes(":ACQ"+the_channel_id+":mem?\n","utf-8")

        post(a_serial=the_serial, a_command=the_command)
        wait_for_data(obj=the_serial,iter_max=1000)
        
        the_reply_sequence=the_serial.readlines()
        the_reply=b''
        for the_index in range(len(the_reply_sequence)):
            the_reply+=the_reply_sequence[the_index]
   
        if isinstance(the_reply,bytes):            
            the_return=the_reply
        else:
            pass

    else:
        pass

    return the_return
