"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as: 

    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
"""


def has_cycle(head):
    dic = {}
    dic[head] = 0
    tmp = head
    while (tmp.next != None):
        if (tmp.next in dic):
            return True
        else:
            dic[tmp.next]=0
            tmp = tmp.next
    return False