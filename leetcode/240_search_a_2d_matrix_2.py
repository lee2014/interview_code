#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
Example:

Consider the following matrix:

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
Given target = 5, return true.

Given target = 20, return false.
"""

__mtime__ = '2018/12/9'


# Run 116 ms
class Solution(object):
    def _search_matrix(self, up_x, up_y, down_x, down_y, matrix, target):
        if up_x > down_x or up_y > down_y:
            return False
        elif target < matrix[up_x][up_y] or target > matrix[down_x][down_y]:
            return False
        elif target == matrix[up_x][up_y]:
            return True
        elif target == matrix[down_x][down_y]:
            return True
        else:
            mid_x = (up_x + down_x) / 2
            mid_y = (up_y + down_y) / 2

            if matrix[mid_x][mid_y] == target:
                return True
            else:
                if self._search_matrix(mid_x+1, up_y, down_x, mid_y, matrix, target):
                    return True
                if self._search_matrix(up_x, mid_y+1, mid_x, down_y, matrix, target):
                    return True

                if target < matrix[mid_x][mid_y]:
                    return self._search_matrix(up_x, up_y, mid_x, mid_y, matrix, target)
                else:
                    return self._search_matrix(mid_x+1, mid_y+1, down_x, down_y, matrix, target)

    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        m = len(matrix)
        n = 0 if m == 0 else len(matrix[0])

        return self._search_matrix(0, 0, m-1, n-1, matrix, target)


if __name__ == "__main__":
    solution = Solution()
    print solution.searchMatrix([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]], 5)
