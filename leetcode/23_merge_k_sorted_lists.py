#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:
    Input:
        [
          1->4->5,
          1->3->4,
          2->6
        ]
    Output: 1->1->2->3->4->4->5->6
"""

__mtime__ = '2018/11/26'


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


# Run 76 ms
class Solution(object):
    def mergeTwoLists(self, list_a, list_b):
        if list_a is None:
            return list_b
        elif list_b is None:
            return list_a
        else:
            if list_a.val <= list_b.val:
                last_node = new_list = list_a
                list_a = list_a.next
            else:
                last_node = new_list = list_b
                list_b = list_b.next

            while list_a is not None or list_b is not None:
                if list_a is None:
                    last_node.next = list_b
                    list_b = None
                elif list_b is None:
                    last_node.next = list_a
                    list_a = None
                elif list_a.val <= list_b.val:
                    last_node.next = list_a
                    list_a = list_a.next
                    last_node = last_node.next
                    last_node.next = None
                else:
                    last_node.next = list_b
                    list_b = list_b.next
                    last_node = last_node.next
                    last_node.next = None

            return new_list

    def mergeKListByIndice(self, low, high, lists):
        if low == high:
            return lists[low]
        elif high == low + 1:
            return self.mergeTwoLists(lists[low], lists[high])
        elif high == low + 2:
            return self.mergeTwoLists(
                self.mergeKListByIndice(low, low + 1, lists),
                lists[high]
            )
        elif high == low + 3:
            return self.mergeTwoLists(
                self.mergeKListByIndice(low, low + 1, lists),
                self.mergeKListByIndice(high - 1, high, lists)
            )
        else:
            mid = (low + high) / 2

            return self.mergeTwoLists(
                self.mergeKListByIndice(low, mid, lists),
                self.mergeKListByIndice(mid + 1, high, lists)
            )

    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """

        if len(lists) == 0:
            return None

        return self.mergeKListByIndice(0, len(lists) - 1, lists)

if __name__ == "__main__":
    my_test1 = ListNode(1)
    my_test1.next = ListNode(4)
    my_test1.next.next = ListNode(5)

    my_test2 = ListNode(1)
    my_test2.next = ListNode(3)
    my_test2.next.next = ListNode(4)

    my_test3 = ListNode(2)
    my_test3.next = ListNode(6)

    my_tests = [my_test1, my_test2, my_test3]

    my_test = Solution().mergeKLists(my_tests)

    node = my_test
    while node is not None:
        print node.val
        node = node.next
