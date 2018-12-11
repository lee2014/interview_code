#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution,
try coding another solution using the divide and conquer approach, which is more subtle.
"""

__mtime__ = '2018/12/5'


# Run 28 ms
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        cur_sum = 0
        max_sum = nums[0]

        for num in nums:
            if (cur_sum + num) <= 0:
                cur_sum = 0
                max_sum = max([max_sum, num])
            else:
                cur_sum += num
                max_sum = max([max_sum, cur_sum])

        return max_sum
