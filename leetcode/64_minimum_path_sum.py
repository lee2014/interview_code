#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example:

Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.
"""

__mtime__ = '2018/12/23'


# Run 44 ms
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        m = len(grid)
        if m == 0:
            return 0
        n = len(grid[0])

        min_path_sum = [[0 for _ in range(n)] for _ in range(m)]
        min_path_sum[m-1][n-1] = grid[m-1][n-1]

        i = m - 1
        while i >= 0:
            j = n - 1
            while j >= 0:
                if i == m - 1 and j == n - 1:
                    pass
                elif i == m - 1:
                    min_path_sum[i][j] = min_path_sum[i][j+1] + grid[i][j]
                elif j == n - 1:
                    min_path_sum[i][j] = min_path_sum[i+1][j] + grid[i][j]
                else:
                    min_path_sum[i][j] = min([min_path_sum[i][j+1], min_path_sum[i+1][j]]) + grid[i][j]
                j -= 1
            i -= 1

        return min_path_sum[0][0]
