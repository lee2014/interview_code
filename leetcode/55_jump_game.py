#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

Example 1:

Input: [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum
             jump length is 0, which makes it impossible to reach the last index.
"""

__mtime__ = '2018/12/8'


# Run 28 ms
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        n = len(nums)

        if n <= 1:
            return True

        max_pos = 0
        for i, num in enumerate(nums):
            if i == 0:
                max_pos = num
            elif max_pos == i:
                max_pos += num
            elif max_pos > i:
                max_pos = max([max_pos, i + nums[i]])
            else:
                return False

            if max_pos >= n - 1:
                return True

        return False


if __name__ == "__main__":
    print Solution().canJump([3, 2, 1, 0, 4])
