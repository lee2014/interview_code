#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]

"""

__mtime__ = '2018/12/10'

class Solution(object):
    def mid_search(self, first, last, nums, target):
        if first > last:
            return -1
        else:
            mid = (first + last) / 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                return self.mid_search(first, mid-1, nums, target)
            else:
                return self.mid_search(mid+1, last, nums, target)

    def distinct_sort_list(self, nums):
        new_nums = []
        for num in nums:
            if len(new_nums) == 0:
                new_nums.append(num)
            elif new_nums[-1] != num:
                new_nums.append(num)
        return new_nums

    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        sort_nums = self.distinct_sort_list(sorted(nums))
        n = len(sort_nums)
        result = []
        i = 0
        while i < n:
            j = i + 1
            while j < n:
                k = self.mid_search(j+1, n-1, sort_nums, -(sort_nums[i] + sort_nums[j]))
                if k != -1:
                    result.append([sort_nums[i], sort_nums[j], sort_nums[k]])
                j += 1
            i += 1

        return result


if __name__ == "__main__":
    solution = Solution()
    print solution.threeSum([-1, 0, 1, 2, -1, -4])
