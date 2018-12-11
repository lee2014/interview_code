#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Note:

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

Example 1:

Given input matrix = 
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],

rotate the input matrix in-place such that it becomes:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]
Example 2:

Given input matrix =
[
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
], 

rotate the input matrix in-place such that it becomes:
[
  [15,13, 2, 5],
  [14, 3, 4, 1],
  [12, 6, 8, 9],
  [16, 7,10,11]
]

"""

__mtime__ = '2018/11/23'


# Run 24ms
class Solution(object):
    def swap(self, a, b):
        a = a ^ b
        b = a ^ b
        a = a ^ b

    def transform(self, matrix):
        n = len(matrix)

        i = 0
        while i < n:
            j = i + 1
            while j < n:
                matrix[i][j] = matrix[i][j] ^ matrix[j][i]
                matrix[j][i] = matrix[i][j] ^ matrix[j][i]
                matrix[i][j] = matrix[i][j] ^ matrix[j][i]
                j += 1
            i += 1

    def mirror_by_x(self, matrix):
        n = len(matrix)

        i = 0
        while i < n / 2:
            tmp = matrix[i]
            matrix[i] = matrix[n - i - 1]
            matrix[n - i - 1] = tmp
            i += 1

    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """

        self.mirror_by_x(matrix)
        self.transform(matrix)
