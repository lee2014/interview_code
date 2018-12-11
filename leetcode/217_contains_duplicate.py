#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Given an array of integers, find if the array contains any duplicates.

Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

Example 1:

Input: [1,2,3,1]
Output: true
Example 2:

Input: [1,2,3,4]
Output: false
Example 3:

Input: [1,1,1,3,3,4,3,2,4,2]
Output: true
"""

__mtime__ = '2018/12/8'


# Run 28 ms
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        mapping = {}
        for num in nums:
            if num in mapping:
                return True
            else:
                mapping[num] = 1
        return False
