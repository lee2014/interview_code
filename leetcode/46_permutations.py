#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Given a collection of distinct integers, return all possible permutations.

Example:
    Input: [1,2,3]
    Output:
        [
          [1,2,3],
          [1,3,2],
          [2,1,3],
          [2,3,1],
          [3,1,2],
          [3,2,1]
        ]
"""

__mtime__ = '2018/11/23'


# Run 40ms
class Solution(object):
    def __init__(self):
        self.nums_list = []

    def find_possible_permutation(self, left_nums, target_nums):
        if len(left_nums) == 0:
            self.nums_list.append(list(target_nums))
            return
        else:
            for idx, num in enumerate(left_nums):
                next_left_nums = list(left_nums)
                del next_left_nums[idx]
                target_nums.append(num)
                self.find_possible_permutation(next_left_nums, target_nums)
                del target_nums[-1]

    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        self.nums_list = []

        for i, num in enumerate(nums):
            next_left_nums = list(nums)
            del next_left_nums[i]
            self.find_possible_permutation(next_left_nums, [num])

        return self.nums_list
