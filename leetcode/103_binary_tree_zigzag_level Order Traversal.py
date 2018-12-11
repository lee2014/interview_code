#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]
"""

__mtime__ = '2018/12/6'


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Run 24 ms
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        node_stack = []
        result_list = []
        flag = 0

        if root is not None:
            node_stack.append(root)

        while len(node_stack) != 0:
            result = []
            new_stack = []
            while len(node_stack) != 0:
                node = node_stack.pop()
                result.append(node.val)

                if flag == 0:
                    if node.left is not None:
                        new_stack.append(node.left)
                    if node.right is not None:
                        new_stack.append(node.right)
                else:
                    if node.right is not None:
                        new_stack.append(node.right)
                    if node.left is not None:
                        new_stack.append(node.left)

            result_list.append(result)
            node_stack = new_stack
            flag = 1 - flag

        return result_list
