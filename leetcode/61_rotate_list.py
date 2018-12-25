#!/usr/bin/env python
# -*- coding: utf-8 -*-

__mtime__ = '2018/12/24'


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# Run 32 ms
class Solution(object):
    def length(self, head):
        if head is None:
            return 0
        else:
            return self.length(head.next) + 1

    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """

        n = self.length(head)
        if n == 0:
            return head
        part_k = k % n

        i = 0
        p = head
        while i < n - part_k - 1:
            p = p.next
            i += 1

        tail = p
        while tail is not None and tail.next is not None:
            tail = tail.next

        if p is not None:
            tail.next = head
            new_head = p.next
            p.next = None
        else:
            new_head = head

        return new_head
