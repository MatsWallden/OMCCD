"""
FUNCTION: FIND AND RETURN A PORT WITH GWafg2005 CONNECTED

AUTHOR: MATS WALLDEN

EMAIL: mats@wallden.eu
"""
import serial
from serial_com.is_device_gwafg2005 import is_device_gwafg2005

def get_serial_gwafg2005(a_port_sequence : list) -> serial.serialposix.Serial:
    """[summary]

    Args:
        a_port_sequence (list): [description]

    Returns:
        serial.serialposix.Serial: [description]
    """
    is_failed=False
    the_return=None

    if is_failed:
        pass
    elif "a_port_sequence" not in locals():
        print("e10c52d8-849c-4256-bb41-5d357fa236c4 \
            input argument a_port_sequence is missing")
        is_failed=True
    elif not isinstance(a_port_sequence,list) or\
        len(a_port_sequence)<1:
        print("eb469095-2063-45fe-bdb3-6a28c080b94e \
            the_port_sequence is not list or empty")
        is_failed=True
    else:
        the_port_sequence=a_port_sequence

    if is_failed:
        pass
    else:
        is_found=False
        for the_port in the_port_sequence:
            if is_failed:
                pass
            elif is_found:
                pass
            elif not isinstance(the_port,str) or\
                len(the_port)<1:
                print("7e83a026-cd33-46e8-a0ed-15609ebde184 \
                    the_port was not string or was empty")
                is_failed=True
            else:
                the_serial=serial.Serial(port=the_port, timeout=0.1)

            if is_failed:
                pass
            elif is_found:
                pass
            elif not isinstance(the_serial,serial.serialposix.Serial) or\
                not the_serial.is_open:
                print("2a13fc6d-94b2-4347-9104-cee0a4803e76 \
                    the_serial was not a serial.serialposix.Serial \
                    or was closed")
                is_failed=True
            else:
                is_found=is_device_gwafg2005(obj=the_serial)

            if is_failed:
                pass
            elif not isinstance(is_found,bool):
                print("4018f35e-bb55-46e3-80c5-63c38ebe284e \
                    is_found was not a boolean")
            elif is_found:
                the_return=the_serial
            else:
                pass

    return the_return
