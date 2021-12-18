"""[module contains function get_port_sequence]
"""
from subprocess import check_output

def get_port_sequence() -> list:
    """[function returns the available ports]

    Returns:
        [list]: [list of available port names]
    """
    is_failed=False
    the_return=None

    if is_failed:
        pass
    else:
        the_ouput_stream=str(check_output(['ls','/dev/'])) #GET ALL  LISTINGS  FOR /dev/

    if is_failed:
        pass
    elif not isinstance(the_ouput_stream,str) or\
        len(the_ouput_stream)<1:
        print("4f8a7ad0-8a3d-480e-baf7-93d851085abd \
            the_ouput_stream was not str or was empty")
        is_failed=True
    else:
        the_output_sequence=the_ouput_stream.split("\\n")

    if is_failed:
        pass
    elif not isinstance(the_output_sequence,list) or\
        len(the_output_sequence)<1:
        print("8dc99bb6-0098-437c-8fd9-4f215727f953 \
            the_output_sequence was not list or was empty")
    else:
        the_port_sequence=[]

        for the_output in the_output_sequence:
            if is_failed:
                pass
            elif not isinstance(the_output,str):
                print("e6032b95-d876-4473-b213-a757adfdc5a9 \
                    the_output was not str")
                is_failed=True
            elif the_output.find('ttyACM')>-1 :
                the_port_sequence.append('/dev/'+the_output)
            else:
                pass

    if is_failed:
        pass
    elif not isinstance(the_port_sequence,list) or\
        len(the_port_sequence)<1:
        print("3dedad9d-4fc3-406c-94c8-45e29a2e3ab3 \
            the_port_sequence was not a list or was empty")
        is_failed=True
    else:
        the_return=the_port_sequence

    return the_return
