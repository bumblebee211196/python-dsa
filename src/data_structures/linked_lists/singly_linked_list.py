"""
singly_linked_list.py: Description of what singly_linked_list.py does.
"""

__author__ = "S Sathish Babu"
__date__ = "25/06/20 Thursday 12:54 PM"
__email__ = "sathish.babu@zohocorp.com"

from typing import List


class Node:
    def __init__(self, val: int, next: "Node" = None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self, head: Node = None):
        self.head = head
        self.len = 0

    def add_to_head(self, val: int) -> None:
        """
        Adds the node to the head

        :param val:     The value to be added
        """
        if not self.head:
            self.head = Node(val)
            self.len += 1
            return
        self.head = Node(val, self.head)
        self.len += 1

    def add_at_index(self, index: int, val: int) -> None:
        """
        Adds the node to the given index, if the index is valid

        :param index:   The position
        :param val:     The value to be added
        """
        if index == 0:
            self.add_to_head(val)
        elif 0 < index <= self.len:
            curr = self.head
            for i in range(index - 1):
                curr = curr.next
            curr.next = Node(val, curr.next)
            self.len += 1

    def remove_head(self) -> None:
        """
        Removes the head node if there exists one
        """
        if self.len > 0:
            self.head = self.head.next
            self.len -= 1

    def remove_at_index(self, index: int) -> None:
        """
        Removes the node at the given index if there exists one

        :param index:   The position
        """
        if index == 0:
            self.remove_head()
        elif 0 < index < self.len:
            curr = self.head
            for i in range(index - 1):
                curr = curr.next
            curr.next = curr.next.next
            self.len -= 1


def array_to_list(values: List[int]) -> LinkedList:
    llist = LinkedList()
    for i in range(len(values) - 1, -1, -1):
        llist.add_to_head(values[i])
    return llist


def list_to_array(llist: LinkedList) -> List[int]:
    curr, values = llist.head, []
    while curr:
        values.append(curr.val)
        curr = curr.next
    return values
