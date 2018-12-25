#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
Example 1:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
Output: true
Example 2:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 13
Output: false
"""

__mtime__ = '2018/12/24'


# Run 24 ms
class Solution(object):
    def _mid_search_matrix(self, matrix, low, high, target, col_nums):
        def _get_index(idx, n):
            return idx / n, idx % n

        if low > high:
            return False
        else:
            mid = (low + high) / 2
            i, j = _get_index(mid, col_nums)
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                return self._mid_search_matrix(matrix, low, mid-1, target, col_nums)
            else:
                return self._mid_search_matrix(matrix, mid+1, high, target, col_nums)

    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        m = len(matrix)
        if m == 0:
            return False

        n = len(matrix[0])
        if n == 0:
            return False

        return self._mid_search_matrix(matrix, 0, n*m - 1, target, n)


if __name__ == "__main__":
    print Solution().searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]], 3)
