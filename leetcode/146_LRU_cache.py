#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

Follow up:
Could you do both operations in O(1) time complexity?

Example:

LRUCache cache = new LRUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.put(4, 4);    // evicts key 1
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4
"""

__mtime__ = '2018/12/6'


class LRUCache(object):
    class DoubleLinkedNode(object):
        def __init__(self, x):
            self.val = x
            self.pre = None
            self.nxt = None

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.len = 0
        self.hash = {}
        self.head = None

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """

        if key in self.hash:
            # update double-linked-queue
            return self.hash[key].val
        else:
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """

        if key in self.hash:
            # update double-linked-queue
            pass
        elif self.len == self.capacity:
            # delete the tail of double-linked-queue

            # delete key in hash

            # len - 1

            # add double-linked-queue

            # add key in hash
            pass
        elif self.len < self.capacity:
            # update the head of double-linked-queue

            # add key in map
            pass

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
