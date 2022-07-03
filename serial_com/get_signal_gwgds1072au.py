"""[summary]
"""
from struct import unpack
def get_signal_gwgds1072au(a_signal_packed: bytes, a_scale : float ) -> list:
    """[function unpacks a signal output form ]

    Args:
        a_serial (serial.serialposix.Serial): [description]
        a_scale (float): [description]

    Returns:
        list: [description]
    """
    the_return = None
    the_signal_packed=a_signal_packed
    the_scale=a_scale
    the_signal_sequence=[]
    the_signal=0.0 #TODO reminder check this before allowing it
    the_info=[]
    n=4
    bla=0
    blb=bla+n
    print(the_signal_packed)
    JX=unpack('>%sh' % 2 ,the_signal_packed[bla:blb])
    for ii in range(0,2003):
        the_info.append(unpack('>%sh' % 2 ,the_signal_packed[bla:blb])[0])
        bla=bla+n
        blb=blb+n
    #TODO get the potential scale
    #TODO get the offset
    #TODO get the time scale

    return the_info
# """[summary]
# """
# from struct import unpack_from
# def get_signal_gwgds1072au(a_signal_packed: bytes, a_scale : float ) -> list:
#     """[function unpacks a signal output form ]

#     Args:
#         a_serial (serial.serialposix.Serial): [description]
#         a_scale (float): [description]

#     Returns:
#         list: [description]
#     """
#     the_return = None
#     the_signal_packed=a_signal_packed
#     the_scale=a_scale
#     the_signal_sequence=[]
#     the_signal=0.0 #TODO reminder check this before allowing it
#     bla=unpack_from('>f',buffer=the_signal_packed,offset=14)
#     raise Exception(bla)
#     if True : #TODO fill in all conditions here
#         the_index_data=14
#         while the_index_data < 8014 :
#             try:
#                 the_signal=unpack_from('>h',buffer=the_signal_packed,offset=the_index_data)
#             except Exception as err:
#                 print(the_index_data)
#                 pass
#                 #print(err)

#             the_signal_sequence.append((the_signal[0]/127.0)*(5*the_scale))

#             the_index_data+=2
#         the_return=the_signal_sequence
#     else :
#         pass

#     return the_return
