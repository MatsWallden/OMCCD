"""[summary]
"""
from serial_com.channelgwgds1072au   import  ChannelGwdGds1072Au
from serial_com.post import post
import serial

def set_potential_offset_gwgds1072au(a_serial: serial.serialposix.Serial,a_channel : ChannelGwdGds1072Au, a_potential_offset: float) -> None:
    the_serial=a_serial
    the_channel=a_channel
    the_potential_offset=a_potential_offset
    the_command=bytes(':'+str(the_channel.name)+':offset '+str(the_potential_offset)+'\n','utf-8')
    post(a_serial=the_serial,a_command=the_command)
