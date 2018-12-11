#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order and each of their nodes contain a single digit.
 Add the two numbers and return it as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:
    Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
    Output: 7 -> 0 -> 8
    Explanation: 342 + 465 = 807.
"""

__mtime__ = '2018/11/22'


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return str(self.val) + "," + str(self.next) if self.next is not None else ""


# Run 68 ms
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        local_l1 = l1
        local_l2 = l2
        new_list = current_node = ListNode(local_l1.val + local_l2.val)

        local_l1 = local_l1.next
        local_l2 = local_l2.next
        while local_l1 is not None or local_l2 is not None:
            if local_l1 is not None and local_l2 is not None:
                current_node.next = ListNode(local_l1.val + local_l2.val)
                local_l1 = local_l1.next
                local_l2 = local_l2.next
            elif local_l1 is not None:
                current_node.next = ListNode(local_l1.val)
                local_l1 = local_l1.next
            else:
                current_node.next = ListNode(local_l2.val)
                local_l2 = local_l2.next

            over_digit = current_node.val / 10
            if over_digit != 0:
                current_node.val = current_node.val % 10
            current_node = current_node.next
            current_node.val = current_node.val + over_digit

        if current_node.val >= 10:
            current_node.next = ListNode(current_node.val / 10)
            current_node.val = current_node.val % 10

        return new_list

if __name__ == "__main__":
    l1 = ListNode(5)
    l2 = ListNode(5)

    solution = Solution()

    print solution.addTwoNumbers(l1, l2)
