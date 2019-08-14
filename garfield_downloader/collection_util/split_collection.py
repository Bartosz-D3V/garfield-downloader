""" split_collection module

Defines split_collection function

"""

from typing import List


def split_collection(collection: List, size: int) -> List[List[str]]:
    """
    Split List into sub lists
    Does not retain order
    :param collection: List
    :param size: int
    :return: List[List[str]]
    """
    return [collection[i::size] for i in range(size)]
