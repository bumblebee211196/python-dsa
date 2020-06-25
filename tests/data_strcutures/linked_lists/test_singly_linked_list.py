"""
test_singly_linked_list.py: Description of what test_singly_linked_list.py does.
"""

__author__ = "S Sathish Babu"
__date__ = "25/06/20 Thursday 12:54 PM"
__email__ = "sathish.babu@zohocorp.com"

from data_structures.linked_lists.singly_linked_list import (
    array_to_list,
    list_to_array,
)


def test_add_to_head():
    cases = [
        (array_to_list([]), 5, array_to_list([5])),
        (array_to_list([1, 2, 3, 4]), 5, array_to_list([5, 1, 2, 3, 4])),
    ]
    for case in cases:
        input_list, val, res_list = case
        input_list.add_to_head(val)
        assert list_to_array(input_list) == list_to_array(res_list)


def test_add_at_index():
    cases = [
        (array_to_list([1, 2, 3, 4]), 0, 5, array_to_list([5, 1, 2, 3, 4])),
        (array_to_list([1, 2, 3, 4]), 1, 5, array_to_list([1, 5, 2, 3, 4])),
        (array_to_list([1, 2, 3, 4]), 2, 5, array_to_list([1, 2, 5, 3, 4])),
        (array_to_list([1, 2, 3, 4]), 3, 5, array_to_list([1, 2, 3, 5, 4])),
        (array_to_list([1, 2, 3, 4]), 4, 5, array_to_list([1, 2, 3, 4, 5])),
    ]
    for case in cases:
        input_list, index, val, res_list = case
        input_list.add_at_index(index, val)
        assert list_to_array(input_list) == list_to_array(res_list)


def test_remove_head():
    cases = [
        (array_to_list([]), array_to_list([])),
        (array_to_list([1]), array_to_list([])),
        (array_to_list([1, 2, 3, 4]), array_to_list([2, 3, 4])),
    ]
    for case in cases:
        input_list, res_list = case
        input_list.remove_head()
        assert list_to_array(input_list) == list_to_array(res_list)


def test_remove_at_index():
    cases = [
        (array_to_list([1, 2, 3, 4, 5]), 0, array_to_list([2, 3, 4, 5])),
        (array_to_list([1, 2, 3, 4, 5]), 1, array_to_list([1, 3, 4, 5])),
        (array_to_list([1, 2, 3, 4, 5]), 2, array_to_list([1, 2, 4, 5])),
        (array_to_list([1, 2, 3, 4, 5]), 3, array_to_list([1, 2, 3, 5])),
        (array_to_list([1, 2, 3, 4, 5]), 4, array_to_list([1, 2, 3, 4])),
    ]
    for case in cases:
        input_list, index, res_list = case
        input_list.remove_at_index(index)
        assert list_to_array(input_list) == list_to_array(res_list)
