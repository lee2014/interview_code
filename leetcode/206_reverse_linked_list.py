#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?
"""

__mtime__ = '2018/12/8'

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# Run 20 ms
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        pre = None
        cur = head

        while cur is not None:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp

        return pre
