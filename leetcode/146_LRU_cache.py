#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Design and implement a data structure for Least Recently Used (LRU) cache.
It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present.
When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

Follow up:
Could you do both operations in O(1) time complexity?

Example:

LRUCache cache = new LRUCache( 2 /* capacity */ )

cache.put(1, 1)
cache.put(2, 2)
cache.get(1)       // returns 1
cache.put(3, 3)    // evicts key 2
cache.get(2)       // returns -1 (not found)
cache.put(4, 4)    // evicts key 1
cache.get(1)       // returns -1 (not found)
cache.get(3)       // returns 3
cache.get(4)       // returns 4
"""

__mtime__ = '2018/12/6'


class DoubleLinkedNode(object):
    def __init__(self, k, v):
        self.key = k
        self.val = v
        self.pre = None
        self.nxt = None

    def get_key(self):
        return self.key

    def get_value(self):
        return self.val

    def set_value(self, v):
        self.val = v


class DoubleLinkedList(object):
    def __init__(self):
        self.head = None

    def __str__(self):
        string = "" if self.head is None else str(self.head.get_value())
        pointer = self.head if self.head is None else self.head.nxt
        while pointer != self.head:
            string += "->" + str(pointer.get_value())
            pointer = pointer.nxt

        return string

    def delete_node(self, node):
        if node == self.head and self.head.pre == self.head:
            self.head = None
        elif node == self.head:
            self.head = self.head.nxt
            self.head.pre = node.pre
            node.nxt = None
            node.pre = None
        else:
            node.pre.nxt = node.nxt
            node.nxt.pre = node.pre
            node.nxt = None
            node.pre = None

        return node

    def delete_tail_node(self):
        tail = None
        if self.head is not None:
            tail = self.head.pre
            self.delete_node(tail)
        return tail

    def insert_val_in_head(self, k, v):
        node = DoubleLinkedNode(k, v)

        if self.head is None:
            self.head = node
            self.head.nxt = node
            self.head.pre = node
        else:
            node.nxt = self.head
            node.pre = self.head.pre
            self.head.pre.nxt = node
            self.head.pre = node
            self.head = node

        return node

    def insert_val_in_tail(self, k, v):
        node = DoubleLinkedNode(k, v)

        if self.head is None:
            self.head = node
            self.head.nxt = node
            self.head.pre = node
        else:
            tail = self.head.pre
            tail.nxt = node
            node.nxt = self.head
            node.pre = tail
            self.head.pre = node

        return node

    def move_node_to_head(self, node):
        if node != self.head:
            node.pre.nxt = node.nxt
            node.nxt.pre = node.pre
            node.nxt = self.head
            node.pre = self.head.pre
            self.head.pre.nxt = node
            self.head.pre = node
            self.head = node


# Run 148 ms
class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.len = 0
        self.hash = {}
        self.double_linked_list = DoubleLinkedList()

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """

        if key in self.hash:
            # update double-linked-queue
            node = self.hash[key]
            self.double_linked_list.move_node_to_head(node)
            return node.get_value()
        else:
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """

        if key in self.hash:
            node = self.hash[key]
            self.double_linked_list.move_node_to_head(node)
            node.set_value(value)
        elif self.len == self.capacity:
            # delete the tail of double-linked-queue
            tail = self.double_linked_list.delete_tail_node()

            # delete tail in hash
            del self.hash[tail.get_key()]

            # add double-linked-queue
            node = self.double_linked_list.insert_val_in_head(key, value)

            # add key in hash
            self.hash[key] = node

        elif self.len < self.capacity:
            # update the head of double-linked-queue
            node = self.double_linked_list.insert_val_in_head(key, value)

            # len + 1
            self.len += 1

            # add key in map
            self.hash[key] = node


if __name__ == "__main__":
    cache = LRUCache(2)

    cache.put(1, 1)
    print "List: " + str(cache.double_linked_list)
    cache.put(2, 2)
    print "List: " + str(cache.double_linked_list)
    print cache.get(1)
    print "List: " + str(cache.double_linked_list)
    cache.put(3, 3)
    print "List: " + str(cache.double_linked_list)
    print cache.get(2)
    print "List: " + str(cache.double_linked_list)
    cache.put(4, 4)
    print "List: " + str(cache.double_linked_list)
    print cache.get(1)
    print "List: " + str(cache.double_linked_list)
    print cache.get(3)
    print "List: " + str(cache.double_linked_list)
    print cache.get(4)
