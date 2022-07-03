"""[module contains function get_time_scale_acquisition]
"""
from struct import unpack
def get_time_scale_acquisition_gwgds1072au(a_signal_packed : bytes)-> float:
    """[function extracts time scale information for an acquistion and scales to seconds]

    Args:
        a_signal_packed (bytes): [description]

    Returns:
        float: [description]
    """    
    the_return = None
    the_signal_packed = a_signal_packed
    #TODO sanity check
    the_return=unpack('>f',the_signal_packed[6:10])[0]/4e-3 #UNPACKS THE BYTES ASSOCIATED WITH THE TIME INTERVAL!
    return the_return
