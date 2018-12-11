#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Given a singly linked list, determine if it is a palindrome.

Example 1:

Input: 1->2
Output: false
Example 2:

Input: 1->2->2->1
Output: true
Follow up:
Could you do it in O(n) time and O(1) space?
"""

__mtime__ = '2018/12/7'


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# Run 96 ms
class Solution(object):
    def reverse_list(self, head):
        if head is None or head.next is None:
            return head, head

        new_head, new_tail = self.reverse_list(head.next)
        new_tail.next = head
        head.next = None
        return new_head, head

    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        def len_list_node(node):
            length = 0
            curr = node
            while curr is not None:
                length += 1
                curr = curr.next
            return length

        if head is None or head.next is None:
            return True

        len_list = len_list_node(head)
        mid = len_list / 2 if len_list % 2 == 0 else len_list / 2 + 1

        mid_node = head
        for _ in range(mid):
            mid_node = mid_node.next
        new_mid_node, _ = self.reverse_list(mid_node)

        p0 = head
        p1 = new_mid_node
        while p0 is not None and p1 is not None:
            if p0.val != p1.val:
                return False
            p0 = p0.next
            p1 = p1.next

        return True
