#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
But the following [1,2,2,null,3,null,3] is not:
    1
   / \
  2   2
   \   \
   3    3
Note:
Bonus points if you could solve it both recursively and iteratively.
"""

__mtime__ = '2018/12/5'


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Run 24 ms
class Solution(object):
    def reverse_tree(self, root_node):
        if root_node is not None:
            left = root_node.left
            right = root_node.right
            root_node.left = right
            root_node.right = left

            self.reverse_tree(root_node.left)
            self.reverse_tree(root_node.right)

    def compare(self, tree1, tree2):
        if tree1 is None and tree2 is None:
            return True
        elif tree1 is None or tree2 is None:
            return False
        elif tree1.val != tree2.val:
            return False
        else:
            return self.compare(tree1.left, tree2.left) and self.compare(tree1.right, tree2.right)

    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        if root is None:
            return True

        root_left = root.left
        root_right = root.right

        self.reverse_tree(root_right)
        return self.compare(root_left, root_right)
