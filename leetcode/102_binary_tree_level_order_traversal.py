#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
"""

__mtime__ = '2018/12/5'


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Run 28 ms
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        node_stack = []

        if root is None:
            return []

        node_stack.append(root)
        result = []

        while len(node_stack) != 0:
            level_result = []
            new_stack = []
            for node in node_stack:
                level_result.append(node.val)
                if node.left is not None:
                    new_stack.append(node.left)
                if node.right is not None:
                    new_stack.append(node.right)
            node_stack = new_stack
            result.append(level_result)

        return result
