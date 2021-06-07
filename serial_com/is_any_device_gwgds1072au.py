"""[summary]
"""
from serial_com.is_device_gwgds1072au import is_device_gwgds1072au
import serial
def is_any_device_gwgds1072au(a_port_sequence: list): 
    """[summary]

    Args:
        a_port_sequence (list): [description]

    Returns:
        [type]: [description]
    """    """[summary]
    """
    the_port_sequence=a_port_sequence

    if the_port_sequence is None:
        return None
    elif str(type(the_port_sequence))!="<class 'list'>":
        return None
    elif len(the_port_sequence) < 1:
        return None
    else:
        pass
    is_it=False
    for the_port in the_port_sequence:
        is_it= is_it | is_device_gwgds1072au(obj=serial.Serial(the_port,timeout=0.1)) 
    return is_it