"""[summary]

    Returns:
        [type]: [description]
"""
from subprocess import check_output

def get_port_sequence() -> list:
    """[summary]

    Returns:
        [type]: [list of port names]
    """
    the_output_raw=str(check_output(['ls','/dev/'])) #GET ALL  LISTINGS  FOR /dev/
    the_port_sequence=None
    if the_output_raw is None :
        the_port_sequence=None
    else:
        the_output_sequence=the_output_raw.split("\\n")

        the_port_sequence=[]

        for the_output in the_output_sequence:

            if the_output.find('ttyACM')>-1 :
                the_port_sequence.append('/dev/'+the_output)
            else:
                pass

    return the_port_sequence
