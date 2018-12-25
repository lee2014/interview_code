#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Given an integer, write a function to determine if it is a power of two.

Example 1:

Input: 1
Output: true 
Explanation: 20 = 1
Example 2:

Input: 16
Output: true
Explanation: 24 = 16
Example 3:

Input: 218
Output: false
"""

__mtime__ = '2018/12/25'


# Run 40 ms
class Solution(object):
    def __init__(self):
        self.power_of_two = [1 for i in range(32)]

        for i, num in enumerate(self.power_of_two):
            if i != 0:
                self.power_of_two[i] = self.power_of_two[i-1] * 2

    def __mid_search(self, l, h, nums, target):
        if l > h:
            return -1
        else:
            mid = (l + h) / 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                return self.__mid_search(l, mid-1, nums, target)
            else:
                return self.__mid_search(mid+1, h, nums, target)

    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """

        if n <= 0:
            return False
        else:
            return self.__mid_search(0, 31, self.power_of_two, n) != -1
