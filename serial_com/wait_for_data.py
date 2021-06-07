
"""
FUNCTION: WAITS FOR DATA FROM SERIAL PORT

AUTHOR: MATS WALLDEN

EMAIL:mats@wallden.eu

"""
from time import sleep
def wait_for_data(obj : 'serial.Serial',iter_max : int =1000) -> None:
    """[summary]

    Args:
        obj ([type]): [serial.Serial object that represents a device]
        iter_max (int, optional): [the maximum number of iterations]. Defaults to 1000.

    Returns:
        [type]: [description]
    """
    data_available=False
    the_iterator=0 #INITIALIZE THE ITERATOR TO 0
    the_condition=True
    while the_condition:
        if the_iterator>iter_max:
            print("EXCEEDED NUMBER OF INTERATIONS WHEN WAITING FOR DATA")
            the_condition=False
            data_available=False
        elif data_available :
            the_condition=False
        else:
            data_available=obj.in_waiting==0
            sleep(0.001)
            the_iterator+=1 #INCREMENTS THE ITERATOR

    return data_available
