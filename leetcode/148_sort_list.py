#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
Sort a linked list in O(n log n) time using constant space complexity.

Example 1:

Input: 4->2->1->3
Output: 1->2->3->4
Example 2:

Input: -1->5->3->4->0
Output: -1->0->3->4->5
"""

__mtime__ = '2018/12/6'


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


# Run 188 ms
class Solution(object):
    def mid_node(self, node):
        if node is None or node.next is None:
            return node

        first = node
        second = first.next

        while second is not None and second.next is not None:
            second = second.next
            if second is not None:
                second = second.next

            first = first.next

        return first

    def merge_sort(self, head1, head2):
        if head1 is None:
            head = head2
        elif head2 is None:
            head = head2
        else:
            h1 = head1
            h2 = head2
            if h1.val > h2.val:
                cur = h2
                h2 = h2.next
            else:
                cur = h1
                h1 = h1.next
            head = cur

            while h1 is not None and h2 is not None:
                if h1.val > h2.val:
                    cur.next = h2
                    h2 = h2.next
                else:
                    cur.next = h1
                    h1 = h1.next

                cur = cur.next

            if h1 is not None:
                cur.next = h1
            if h2 is not None:
                cur.next = h2

        return head

    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if head is None or head.next is None:
            return head

        mid = self.mid_node(head)
        mid_next = None
        if mid is not None:
            mid_next = mid.next
            mid.next = None

        node1 = self.sortList(head)
        node2 = self.sortList(mid_next)

        return self.merge_sort(node1, node2)

if __name__ == "__main__":
    test = ListNode(4)
    test.next = ListNode(3)
    test.next.next = ListNode(2)
    test.next.next.next = ListNode(1)

    result = Solution().sortList(test)

    while result is not None:
        print result.val
        result = result.next
