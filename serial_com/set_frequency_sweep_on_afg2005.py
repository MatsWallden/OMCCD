# """[summary]
# """
# from serial_com.post import post
# import serial

# def set_frequency_sweep_on_afg2005(a_serial: serial.serialposix.Serial)-> None:
#     """[summary]

#     Args:
#         a_serial (serial.serialposix.Serial): [description]
#     """    
#     the_serial=a_serial
#     the_command=b'SOUR1:SWE:STAT ON\n'
#     post(a_serial=the_serial,a_command=the_command)
