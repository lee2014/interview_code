#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Given an array of size n, find the majority element.
The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3
Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2
"""

__mtime__ = '2018/12/7'


# Run 32 ms
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        count = 0
        cur_num = 0
        for i, num in enumerate(nums):
            if count == 0:
                cur_num = num
                count = 1
            elif cur_num == num:
                count += 1
            else:
                count -= 1

        return cur_num
