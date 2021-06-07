"""[summary]
"""

class Device():
    """[a representation for a device connected over a serial communication port]

    Args:
        object (['Device']): []
        a_id (['str']) : [an identifier]
    """
    def __init__(self, a_id : str):
        """[summary]

        Args:
            a_id (str): [identifier for the device]
        """
        self.__initialize_id(a_id)

    def __initialize_id(self, a_id : str )-> None:
        """[initialize member variable __id]

        Args:
            a_id (str): [identifier for the device]
        """
        self.__id=a_id

    def get_id(self)->str:
        """[returns the identifier]

        Returns:
            [str]: [description]
        """
        return self.__id

    def post(self, a_command : str ) -> None:
        """[posts a command to a Device]

        Args:
            a_command (str): [a command to post to a device]
        """

    def read(self) -> None:
        """[reads from a Device]
        """
