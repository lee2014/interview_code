#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Given a sorted array and a target value, return the index if the target is found. 
If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Example 1:
    Input: [1,3,5,6], 5
    Output: 2

Example 2:
    Input: [1,3,5,6], 2
    Output: 1

Example 3:
    Input: [1,3,5,6], 7
    Output: 4

Example 4:
    Input: [1,3,5,6], 0
    Output: 0
"""

__mtime__ = '2018/11/23'


# Run 24ms
class Solution(object):
    def search_insert_position_list(self, low, high, array, value):
        if (low + high) % 2 == 0:
            mid = (low + high) / 2
            if value == array[mid]:
                return (low + high) / 2
            elif value > array[mid]:
                return self.search_insert_position_list(mid, high, array, value)
            else:
                return self.search_insert_position_list(low, mid, array, value)
        else:
            mid_pre = (low + high) / 2
            mid_suf = (low + high) / 2 + 1
            if array[mid_pre] == value:
                return mid_pre
            elif array[mid_suf] == value:
                return mid_suf
            elif array[mid_pre] < value < array[mid_suf]:
                return mid_suf
            elif value > array[mid_suf]:
                return self.search_insert_position_list(mid_suf, high, array, value)
            else:
                return self.search_insert_position_list(low, mid_pre, array, value)

    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        nums_len = len(nums)

        if nums_len == 0 or target < nums[0]:
            return 0
        elif target > nums[nums_len - 1]:
            return nums_len
        else:
            return self.search_insert_position_list(0, nums_len - 1, nums, target)
