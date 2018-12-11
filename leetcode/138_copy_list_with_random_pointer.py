#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list.
"""

__mtime__ = '2018/12/6'


# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


# Run 68 ms
class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """

        if head is None:
            return None

        cur_node = head
        random_head = random_curr = RandomListNode(cur_node.label)
        node_map = {cur_node: random_curr}

        cur_node = cur_node.next
        while cur_node is not None:
            random_curr.next = RandomListNode(cur_node.label)
            random_curr = random_curr.next
            node_map[cur_node] = random_curr
            cur_node = cur_node.next

        cur_node = head
        random_curr = random_head
        while cur_node is not None:
            if cur_node.random in node_map:
                random_curr.random = node_map[cur_node.random]
            cur_node = cur_node.next
            random_curr = random_curr.next

        return random_head
