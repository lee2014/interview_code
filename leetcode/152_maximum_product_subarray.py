#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

Example 1:

Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
"""

__mtime__ = '2018/12/6'


# Run 48 ms
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        max_product = nums[0]
        cur_max = 0
        cur_min = 0
        for i, num in enumerate(nums):
            if num == 0:
                cur_max = 0
                cur_min = 0
            elif cur_max == 0:
                cur_max = cur_min = num
            else:
                tmp_max = max([cur_max * num, cur_min * num, num])
                tmp_min = min([cur_max * num, cur_min * num, num])
                cur_max = tmp_max
                cur_min = tmp_min

            max_product = max([max_product, cur_max])

        return max_product


if __name__ == "__main__":
    print Solution().maxProduct([-4, -3, -2])
