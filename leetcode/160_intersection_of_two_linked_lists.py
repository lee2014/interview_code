#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Write a program to find the node at which the intersection of two singly linked lists begins.


For example, the following two linked lists:

A:          a1 → a2
                   ↘
                     c1 → c2 → c3
                   ↗            
B:     b1 → b2 → b3
begin to intersect at node c1.


Notes:

If the two linked lists have no intersection at all, return null.
The linked lists must retain their original structure after the function returns.
You may assume there are no cycles anywhere in the entire linked structure.
Your code should preferably run in O(n) time and use only O(1) memory.
"""

__mtime__ = '2018/12/6'


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Run 236 ms
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type headA, headB: ListNode
        :rtype: ListNode
        """

        def length_list_node(head):
            length = 0
            cur = head
            while cur is not None:
                length += 1
                cur = cur.next

            return length

        len_A = length_list_node(headA)
        len_B = length_list_node(headB)

        if len_A == 0 or len_B == 0:
            return None

        if len_A > len_B:
            big_head = headA
            small_head = headB
        else:
            big_head = headB
            small_head = headA

        first_step = len_A - len_B if len_A > len_B else len_B - len_A

        for _ in range(first_step):
            big_head = big_head.next

        while big_head is not None and small_head is not None and big_head != small_head:
            big_head = big_head.next
            small_head = small_head.next

        return big_head
