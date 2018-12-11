#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Given an array, rotate the array to the right by k steps, where k is non-negative.

Example 1:

Input: [1,2,3,4,5,6,7] and k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:

Input: [-1,-100,3,99] and k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
Note:

Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
Could you do it in-place with O(1) extra space?
"""

__mtime__ = '2018/12/7'


# Run 52 ms
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        def reverse(first, last, array):
            i = first
            j = last
            while i < j:
                array[i] = array[i] ^ array[j]
                array[j] = array[i] ^ array[j]
                array[i] = array[i] ^ array[j]
                i += 1
                j -= 1

        n = len(nums)

        if n == 1:
            return

        k %= n

        reverse(0, n - 1, nums)
        reverse(0, k - 1, nums)
        reverse(k, n - 1, nums)
