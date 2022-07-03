"""
FUNCTION: FIND AND RETURN A PORT WITH GWafg2005 CONNECTED

AUTHOR: MATS WALLDEN

EMAIL: mats@wallden.eu
"""
import serial
from serial_com.is_device_gwafg2005 import is_device_gwafg2005

def get_serial_gwafg2005(a_port_sequence : list) -> serial.serialposix.Serial:
    """[summary test version for exception handling]

    Args:
        a_port_sequence (list): [description]

    Returns:
        serial.serialposix.Serial: [description, \
            will return None if device not found]
    """
    the_return=None

    if "a_port_sequence" not in locals():
        raise NameError("e10c52d8-849c-4256-bb41-5d357fa236c4 \
            input argument a_port_sequence is missing")

    if not isinstance(a_port_sequence,list):
        raise TypeError("eb469095-2063-45fe-bdb3-6a28c080b94e \
            the_port_sequence is not list")

    if len(a_port_sequence)==0:
        raise ValueError("477e7458-7e2a-4382-a8c3-a052207df25d   \
            a_port_sequence was emty")

    the_port_sequence=a_port_sequence

    is_found=False

    for the_port in the_port_sequence:
        if is_found:
            pass
        else:
            if not isinstance(the_port,str):
                raise TypeError("b470e275-cfce-4bbd-b68d-cfe95b275c34   \
                    the_port was not a string")

            if len(the_port)==0:
                raise ValueError("7e83a026-cd33-46e8-a0ed-15609ebde184 \
                    the_port was empty")

            the_serial=serial.Serial(port=the_port, timeout=0.1) #TODO configure timeout

            if not isinstance(the_serial,serial.serialposix.Serial):
                raise TypeError("2a13fc6d-94b2-4347-9104-cee0a4803e76 \
                    the_serial was not a serial.serialposix.Serial")

            if not the_serial.is_open:
                raise ValueError("005b35ac-ea39-41d0-bd51-795fabeed9a4  \
                    the_serial was not open")

            is_found=is_device_gwafg2005(obj=the_serial)

            if not isinstance(is_found,bool):
                raise TypeError("4018f35e-bb55-46e3-80c5-63c38ebe284e \
                    is_found was not a boolean")

            the_return=the_serial

    return the_return
