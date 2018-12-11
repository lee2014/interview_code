#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
"""

__mtime__ = '2018/12/6'


# Run 28 ms
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """

        result_lists = []
        for i in range(numRows):
            n = i + 1
            result_lists.append(
                [1 if j == 0 or j == n - 1 else result_lists[i-1][j] + result_lists[i-1][j-1] for j in range(n)]
            )

        return result_lists
