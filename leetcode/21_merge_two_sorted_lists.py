#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Merge two sorted linked lists and return it as a new list.
The new list should be made by splicing together the nodes of the first two lists.

Example:
    Input: 1->2->4, 1->3->4
    Output: 1->1->2->3->4->4
"""
__mtime__ = '2018/11/23'


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


# Run 24ms
class Solution(object):
    def __init__(self):
        self.HEADER = ListNode(0)

    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        local_l1 = l1
        local_l2 = l2

        new_list = current_node = self.HEADER

        while local_l1 is not None or local_l2 is not None:
            if local_l1 is not None and local_l2 is not None:
                if local_l1.val <= local_l2.val:
                    current_node.next = local_l1
                    local_l1 = local_l1.next
                else:
                    current_node.next = local_l2
                    local_l2 = local_l2.next
            elif local_l1 is not None:
                current_node.next = local_l1
                local_l1 = local_l1.next
            else:
                current_node.next = local_l2
                local_l2 = local_l2.next

            current_node = current_node.next

        return new_list.next

