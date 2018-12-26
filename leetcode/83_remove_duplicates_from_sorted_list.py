#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Given a sorted linked list, delete all duplicates such that each element appear only once.

Example 1:

Input: 1->1->2
Output: 1->2
Example 2:

Input: 1->1->2->3->3
Output: 1->2->3
"""

__mtime__ = '2018/12/26'


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Run 48 ms
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        p = head

        while p is not None:
            if p.next is not None:
                if p.val == p.next.val:
                    p.next = p.next.next
                else:
                    p = p.next
            else:
                p = p.next

        return head
