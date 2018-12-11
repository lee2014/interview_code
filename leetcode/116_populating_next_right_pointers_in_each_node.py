#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Given a binary tree

struct TreeLinkNode {
  TreeLinkNode *left;
  TreeLinkNode *right;
  TreeLinkNode *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

Note:

You may only use constant extra space.
Recursive approach is fine, implicit stack space does not count as extra space for this problem.
You may assume that it is a perfect binary tree (ie, all leaves are at the same level, and every parent has two children).
Example:

Given the following perfect binary tree,

     1
   /  \
  2    3
 / \  / \
4  5  6  7
After calling your function, the tree should look like:

     1 -> NULL
   /  \
  2 -> 3 -> NULL
 / \  / \
4->5->6->7 -> NULL
"""

__mtime__ = '2018/12/6'


# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

# Run 44 ms
class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):

        node_stack = []

        if root is not None:
            node_stack.append(root)

        node_stack.append(None)

        while node_stack[0] is not None:
            new_stack = []
            for i, node in enumerate(node_stack):
                if node is not None:
                    node.next = node_stack[i+1]
                    if node.left is not None:
                        new_stack.append(node.left)
                    if node.right is not None:
                        new_stack.append(node.right)

            new_stack.append(None)
            node_stack = new_stack
