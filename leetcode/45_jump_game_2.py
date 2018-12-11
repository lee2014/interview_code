#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

Example:

Input: [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2.
    Jump 1 step from index 0 to 1, then 3 steps to the last index.
Note:

You can assume that you can always reach the last index.
"""

__mtime__ = '2018/11/28'


# Run 28 ms
class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        n = len(nums)
        if n <= 1 or nums[0] == 0:
            return 0

        least_jump = [0] * n
        j = 1
        for i, num in enumerate(nums):
            max_jump = i + num
            while j < n and j <= max_jump:
                least_jump[j] = least_jump[i] + 1
                j += 1

        return least_jump[n-1]


if __name__ == "__main__":
    print Solution().jump([6, 2, 6, 1, 7, 9, 3, 5, 3, 7, 2, 8, 9, 4, 7, 7, 2, 2, 8, 4, 6, 6, 1, 3])
    print Solution().jump([2, 3, 1, 1, 4])
    print Solution().jump([9,4,5,4,1,8,1,2,0,7,8,7,0,6,6,1,1,2,5,0,9,8,4,7,9,6,8,1,4,0,8,5,5,3,9,8,1,2,2,3,0,1,3,2,7,9,3,0,1])
