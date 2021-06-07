"""[summary]
"""
import serial
def post(a_serial: serial.serialposix.Serial,a_command : bytes ) -> int:
    """[posts to a device]

    Args:
        a_serial (Serial): [a serial object]
        a_command (bytes): [a command]
    """
    the_serial=a_serial
    the_command=a_command
    the_return=None
    if not isinstance(the_serial,serial.serialposix.Serial):
        the_return=None
    elif not the_serial.is_open:
        the_return=None
    elif the_command is None:
        the_return=None
    elif not isinstance(the_command,bytes):
        the_return=None
    else:
        the_return=the_serial.write(the_command)

    return the_return
