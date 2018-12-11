#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Given a linked list, remove the n-th node from the end of list and return its head.

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:

Given n will always be valid.

Follow up:

Could you do this in one pass?
"""

__mtime__ = '2018/11/30'


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


# Run 24 ms
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """

        new_head = ListNode(0)
        new_head.next = head
        cur = head

        i = 0
        while i < n and cur is not None:
            cur = cur.next
            i += 1

        rm_head = new_head
        while cur is not None:
            cur = cur.next
            rm_head = rm_head.next

        if rm_head.next is not None:
            rm_node = rm_head.next
            rm_head.next = rm_node.next
            rm_node.next = None

        return new_head.next


def str_list(head):
    if head is None:
        return ""
    elif head.next is None:
        return str(head.val)
    else:
        return str(head.val) + "->" + str_list(head.next)

if __name__ == "__main__":
    test_head = ListNode(1)
    test_head.next = ListNode(2)

    result = Solution().removeNthFromEnd(test_head, 2)
    print str_list(result)
