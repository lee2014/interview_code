#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Given a binary tree, return the inorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,3,2]
Follow up: Recursive solution is trivial, could you do it iteratively?
"""

__mtime__ = '2018/12/5'


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Run 24 ms
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        node = root
        node_stack = []
        result_list = []

        while node is not None or len(node_stack) != 0:
            while node is not None:
                node_stack.append(node)
                node = node.left

            if len(node_stack) != 0:
                pop_node = node_stack.pop()
                result_list.append(pop_node.val)
                if pop_node.right is not None:
                    node = pop_node.right

        return result_list
