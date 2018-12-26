#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Remove all elements from a linked list of integers that have value val.

Example:

Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5
"""

__mtime__ = '2018/12/26'


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


# Run 64 ms
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """

        empty_head = ListNode(0)
        empty_head.next = head

        p = empty_head

        while p.next is not None:
            if p.next.val == val:
                p.next = p.next.next
            else:
                p = p.next

        return empty_head.next
