#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Reverse a linked list from position m to n. Do it in one-pass.

Note: 1 ≤ m ≤ n ≤ length of list.

Example:

Input: 1->2->3->4->5->NULL, m = 2, n = 4
Output: 1->4->3->2->5->NULL
"""

__mtime__ = '2018/12/24'


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


# Run 24 ms
class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """

        if m == n:
            return head

        empty_head = ListNode(0)
        empty_head.next = head

        i = 0
        m_head = empty_head
        while i < m - 1:
            m_head = m_head.next
            i += 1

        reverse_head = None
        reverse_tail = None
        tail = None
        p = m_head.next
        while i <= n - 1:
            if reverse_head is None:
                reverse_head = p
                reverse_tail = p
                p = p.next
            else:
                tmp = p
                p = p.next
                tmp.next = reverse_head
                reverse_head = tmp
            tail = p
            i += 1

        reverse_tail.next = tail
        m_head.next = reverse_head

        return empty_head.next
