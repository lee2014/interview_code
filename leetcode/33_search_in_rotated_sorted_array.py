#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:
    Input: nums = [4,5,6,7,0,1,2], target = 0
    Output: 4
    
Example 2:
    Input: nums = [4,5,6,7,0,1,2], target = 3
    Output: -1
"""

__mtime__ = '2018/11/23'


# Run 20ms
class Solution(object):
    def search_sorted_list(self, low, high, array, value):
        mid = (low + high) / 2
        if low > high:
            return -1
        elif array[mid] == value:
            return mid
        elif array[mid] > value:
            return self.search_sorted_list(low, mid - 1, array, value)
        else:
            return self.search_sorted_list(mid + 1, high, array, value)

    def search_cycle_sorted_list(self, low, high, array, value):
        mid = (low + high) / 2
        if low > high:
            return -1
        elif array[mid] == value:
            return mid
        elif array[low] <= value <= array[mid]:
            return self.search_sorted_list(low, mid - 1, array, value)
        elif array[mid] <= value <= array[high]:
            return self.search_sorted_list(mid + 1, high, array, value)
        elif array[mid] < array[high]:
            return self.search_cycle_sorted_list(low, mid - 1, array, value)
        elif array[mid] > array[high]:
            return self.search_cycle_sorted_list(mid + 1, high, array, value)
        else:
            return -1

    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        return self.search_cycle_sorted_list(0, len(nums) - 1, nums, target)
