#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Given the following binary tree:  root = [3,5,1,6,2,0,8,null,null,7,4]

        _______3______
       /              \
    ___5__          ___1__
   /      \        /      \
   6      _2       0       8
         /  \
         7   4
Example 1:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.
Example 2:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself
             according to the LCA definition.
Note:

All of the nodes' values will be unique.
p and q are different and both values will exist in the binary tree.
"""

__mtime__ = '2018/12/6'


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# Run 136 ms
class Solution(object):
    def find_path_in_tree(self, node, target, path, result):
        if len(result) != 0:
            return

        path.append(node)
        if node.val == target:
            result.extend(path)

        if node.left is not None:
            self.find_path_in_tree(node.left, target, path, result)
        if node.right is not None:
            self.find_path_in_tree(node.right, target, path, result)
        path.pop()

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        p_path = []
        q_path = []

        self.find_path_in_tree(root, p.val, [], p_path)
        self.find_path_in_tree(root, q.val, [], q_path)

        p_len = len(p_path)
        q_len = len(q_path)

        lowest_common_ancestor = None
        i = 0
        while i < p_len and i < q_len:
            if p_path[i] == q_path[i]:
                lowest_common_ancestor = p_path[i]
            i += 1

        return lowest_common_ancestor
