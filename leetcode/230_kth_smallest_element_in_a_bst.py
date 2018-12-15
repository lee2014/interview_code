#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

Note: 
You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

Example 1:

Input: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
Output: 1
Example 2:

Input: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
Output: 3
Follow up:
What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently?
How would you optimize the kthSmallest routine?
"""

__mtime__ = '2018/12/11'

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# Run 56 ms
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """

        k_smallest_val = []
        self.num_of_node(root, k, k_smallest_val)

        return k_smallest_val[0]

    def num_of_node(self, tree_node, k_smallest, target):
        if tree_node is None:
            return 0
        else:
            left_num = self.num_of_node(tree_node.left, k_smallest, target)
            if left_num + 1 == k_smallest:
                target.append(tree_node.val)
            right_num = self.num_of_node(tree_node.right, k_smallest-left_num-1, target)
            return left_num + right_num + 1

