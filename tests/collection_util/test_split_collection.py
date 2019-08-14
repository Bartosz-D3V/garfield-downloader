""" Unit tests for split_collection module
"""

from garfield_downloader.collection_util.split_collection import split_collection


def test_split_collection_should_split() -> None:
    """
    split_collection should split list into
    sub-lists if possible
    :return: None
    """
    mock_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    splitted_list = split_collection(mock_list, 4)
    assert splitted_list[0] == [0, 4, 8]
    assert splitted_list[1] == [1, 5, 9]
    assert splitted_list[2] == [2, 6]
    assert splitted_list[3] == [3, 7]
