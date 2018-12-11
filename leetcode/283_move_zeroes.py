#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.
"""

__mtime__ = '2018/12/8'


# Run 40 ms
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        n = len(nums)
        unzero = 0
        i = 1
        while i < n and unzero < n:
            while unzero < n and nums[unzero] != 0:
                unzero += 1
            i = max(unzero + 1, i)
            while i < n and nums[i] == 0:
                i += 1

            if i < n:
                nums[i] = nums[i] ^ nums[unzero]
                nums[unzero] = nums[i] ^ nums[unzero]
                nums[i] = nums[i] ^ nums[unzero]
