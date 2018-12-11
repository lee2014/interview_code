#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Given an unsorted integer array, find the smallest missing positive integer.

Example 1:
    Input: [1,2,0]
    Output: 3

Example 2:
    Input: [3,4,-1,1]
    Output: 2

Example 3:
    Input: [7,8,9,11,12]
    Output: 1

Note:
    Your algorithm should run in O(n) time and uses constant extra space.
"""

__mtime__ = '2018/11/23'


# Run 20ms
class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        num_len = len(nums)
        if num_len == 0:
            return 1

        int_set = [0 for _ in range(num_len)]

        for num in nums:
            if 0 < num <= num_len:
                int_set[num - 1] = 1

        for i, flag in enumerate(int_set):
            if flag == 0:
                return i + 1

        return num_len + 1


if __name__ == "__main__":
    solution = Solution()

    print solution.firstMissingPositive([1, 2, 0]) == 3
    print solution.firstMissingPositive([3, 4, -1, 1]) == 2
    print solution.firstMissingPositive([7, 8, 9, 11, 12]) == 1
    print solution.firstMissingPositive([]) == 1
    print solution.firstMissingPositive([1, 2, 3]) == 4
