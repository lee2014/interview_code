#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
iven a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
Example 1:

Input:
    2
   / \
  1   3
Output: true
Example 2:

    5
   / \
  1   4
     / \
    3   6
Output: false
Explanation: The input is: [5,1,4,null,null,3,6]. The root node's value
             is 5 but its right child's value is 4.
"""

__mtime__ = '2018/12/4'


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Run 40 ms
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        valid, _, _ = self.isValid(root)

        return valid

    def isValid(self, node):
        if node.left is None and node.right is None:
            return True, node.val, node.val

        if node.left is None:
            validation, min_val, max_val = self.isValid(node.right)
            return validation and (node.val < min_val), node.val, max_val

        if node.right is None:
            validation, min_val, max_val = self.isValid(node.left)
            return validation and node.val > max_val, min_val, node.val

        l_validation, l_min, l_max = self.isValid(node.left)
        r_validation, r_min, r_max = self.isValid(node.right)

        return l_validation and r_validation and l_max < node.val < r_min, l_min, r_max
