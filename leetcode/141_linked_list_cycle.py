#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Given a linked list, determine if it has a cycle in it.

Follow up:
Can you solve it without using extra space?
"""

__mtime__ = '2018/12/6'


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# Run 44 ms
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        if head is None:
            return False

        first = head
        second = head.next

        while first is not None and second is not None and first != second:
            if second is not None:
                second = second.next
            if second is not None:
                second = second.next

            first = first.next

        return first == second
