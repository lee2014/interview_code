#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

Example:

Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5

Note:

Only constant extra memory is allowed.
You may not alter the values in the list's nodes, only nodes itself may be changed.
"""

__mtime__ = '2018/11/26'


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


# Run 64ms
class Solution(object):
    def reverseHeadNodeByK(self, head, k):
        if head is None:
            return None, None
        elif head.next is None or k <= 1:
            return head, head
        else:
            h, t = self.reverseHeadNodeByK(head.next, k - 1)
            if h is None:
                return head, head
            head.next = t.next
            t.next = head
            t = head
            return h, t

    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """

        if head is None:
            return None

        list_head = ListNode(0)
        list_head.next = head

        def len_large_than_num(head_node, num):
            length = 0
            cur = head_node
            while cur is not None and length < num:
                length += 1
                cur = cur.next

            if length == num:
                return True
            else:
                return False

        # reverse group
        next_group_head = list_head
        while next_group_head is not None and next_group_head.next is not None:
            if len_large_than_num(next_group_head.next, k):
                h, t = self.reverseHeadNodeByK(next_group_head.next, k)
                next_group_head.next = h
                next_group_head = t
            else:
                break

        return list_head.next


if __name__ == "__main__":
    def gen_list_node(num):
        cur = head = ListNode(0)
        for i in range(num):
            cur.next = ListNode(i + 1)
            cur = cur.next

        return head.next

    def str_list_node(head):
        if head is None:
            return ""
        elif head.next is None:
            return str(head.val)
        else:
            return str(head.val) + "->" + str_list_node(head.next)

    test_node_1 = Solution().reverseKGroup(gen_list_node(5), 1)
    test_node_2 = Solution().reverseKGroup(gen_list_node(5), 2)
    test_node_3 = Solution().reverseKGroup(gen_list_node(5), 3)

    print str_list_node(test_node_1) == "1->2->3->4->5"
    print str_list_node(test_node_2) == "2->1->4->3->5"
    print str_list_node(test_node_3) == "3->2->1->4->5"

