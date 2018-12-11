#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
"""

__mtime__ = '2018/12/10'


# Run 28 ms
class Solution(object):
    def subset_by_n(self, nums, n, stack, result):
        if n == 0:
            return result.append(stack)
        elif len(nums) == n:
            return result.append(stack + nums)
        else:
            self.subset_by_n(nums[1:], n - 1, stack + nums[0:1], result)
            self.subset_by_n(nums[1:], n, stack, result)

    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        result = []
        for i in range(len(nums) + 1):
            self.subset_by_n(nums, i, [], result)

        return result
