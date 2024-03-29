"""
FUNCTION: IDENTIFIES A GWINSTEK GWAFG2005 FUNCTION GENERATOR CONNECTED TO A SERIAL PORT
AUTHOR: MATS WALLDEN
EMAIL: mats@wallden.eu
"""
import re #IMPORTS REGULAR EXPRESSIONS MODULE
from serial_com.wait_for_data import wait_for_data #FIX ME HARDCODED PATH
import serial
def is_device_gwgds1072au(obj : serial.serialposix.Serial)  -> bool:
    """[summary]
    the function is used to ascertain if a device is an gwinstek oscilloscope of type gds1072au
    Args:
        obj (serial.Serial): [a serial.Serial object that can be used to communicate with a device]

    Returns:
        bool: [the answer to the question if the device is a gds oscilloscope]
    """
    close_ports=False
    if not obj.is_open:
        obj.open() #OPENS THE SERIAL PORTS IF CLOSED
        close_ports=True #DECISION BASIS CLOSE PORT BEFORE RETURN
    else:
        pass

    obj.reset_input_buffer() #FLUSHES THE INPUT BUFFER
    obj.write(b'*idn?\n')
    wait_for_data(obj) #WAITS FOR DATA
    data=obj.readlines()  #READS THE DATA

    if len(data)<1 :
        is_device = None
    else:
        the_reply=data[0].decode('utf-8')
        the_match=re.match('GW,GDS-1072A-U',the_reply) #SEARCHES THE DATA FOR THE PATTERN
        is_device=not the_match is None#DECISION IS IT THE DEVICE

    if close_ports:   #DECISION TO CLOSE PORT BEFORE RETURN
        obj.close()
    else:
        pass

    return is_device
