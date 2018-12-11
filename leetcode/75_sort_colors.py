#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note: You are not suppose to use the library's sort function for this problem.

Example:

Input: [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Follow up:

A rather straight forward solution is a two-pass algorithm using counting sort.
First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.
Could you come up with a one-pass algorithm using only constant space?
"""

__mtime__ = '2018/12/6'


# Run 24 ms
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        len_nums = len(nums)

        if len_nums <= 1:
            return

        p0 = 0
        p2 = len_nums - 1
        i = 0
        while i <= p2:
            if nums[i] == 2 and i != p2:
                nums[i] = nums[p2] ^ nums[i]
                nums[p2] = nums[p2] ^ nums[i]
                nums[i] = nums[p2] ^ nums[i]
                p2 -= 1
            elif nums[i] == 0:
                if i != p0:
                    nums[i] = nums[p0] ^ nums[i]
                    nums[p0] = nums[p0] ^ nums[i]
                    nums[i] = nums[p0] ^ nums[i]
                p0 += 1
                i += 1
            else:
                i += 1
