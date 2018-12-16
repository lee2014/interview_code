"""
Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.

Example 1:

Input:
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
Output:
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]
Example 2:

Input:
[
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
Output:
[
  [0,0,0,0],
  [0,4,5,0],
  [0,3,1,0]
]
Follow up:

A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?
"""


# Run 124 ms
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """

        m = len(matrix)
        if m == 0:
            return
        n = len(matrix[0])

        zero_x = [1 for _ in range(m)]
        zero_y = [1 for _ in range(n)]

        for i, row in enumerate(matrix):
            for j, cell in enumerate(row):
                if cell == 0:
                    zero_x[i] = 0
                    zero_y[j] = 0

        for i, row in enumerate(matrix):
            for j, _ in enumerate(row):
                if zero_x[i] == 0 or zero_y[j] == 0:
                    matrix[i][j] = 0
