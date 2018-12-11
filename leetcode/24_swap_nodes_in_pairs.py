#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Given a linked list, swap every two adjacent nodes and return its head.

Example:

Given 1->2->3->4, you should return the list as 2->1->4->3.
Note:

Your algorithm should use only constant extra space.
You may not modify the values in the list's nodes, only nodes itself may be changed.
"""

__mtime__ = '2018/11/23'


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


# Run 24ms
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if head is None or head.next is None:
            return head

        new_head = ListNode(0)
        new_head.next = head

        pre_node = new_head
        cur_node = head
        while cur_node is not None and cur_node.next is not None:
            suf_node = cur_node.next

            cur_node.next = suf_node.next
            suf_node.next = cur_node
            pre_node.next = suf_node

            pre_node = cur_node
            cur_node = cur_node.next

        return new_head.next
