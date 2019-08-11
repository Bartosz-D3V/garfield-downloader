""" create_dir module

Defines function used to safely
create a directory

"""

import os


def create_dir(directory: str) -> None:
    """
    Creates a directory if it does not
    exists
    :param directory: str
    :return: None
    """
    if not os.path.exists(directory):
        os.makedirs(directory)
