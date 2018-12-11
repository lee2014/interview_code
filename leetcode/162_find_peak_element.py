#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
A peak element is an element that is greater than its neighbors.

Given an input array nums, where nums[i] ≠ nums[i+1], find a peak element and return its index.

The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

You may imagine that nums[-1] = nums[n] = -∞.

Example 1:

Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.
Example 2:

Input: nums = [1,2,1,3,5,6,4]
Output: 1 or 5 
Explanation: Your function can return either index number 1 where the peak element is 2, 
             or index number 5 where the peak element is 6.
Note:

Your solution should be in logarithmic complexity.
"""

__mtime__ = '2018/12/7'


# Run 20 ms
class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def is_peak(pos, nums):
            if pos == 0 and len(nums) == 1:
                return True
            elif pos == 0:
                return nums[pos] > nums[pos+1]
            elif pos == len(nums) - 1:
                return nums[pos] > nums[pos-1]
            else:
                return nums[pos-1] < nums[pos] and nums[pos+1] < nums[pos]

        len_nums = len(nums)
        if len_nums == 0:
            return -1

        low = 0
        high = len_nums - 1
        while low <= high:
            mid = (low + high) / 2
            if is_peak(mid, nums):
                return mid
            elif mid == high:
                high = mid - 1
            elif mid == low:
                low = mid + 1
            elif nums[mid-1] < nums[mid] < nums[mid+1]:
                low = mid + 1
            elif nums[mid-1] > nums[mid] > nums[mid+1]:
                high = mid - 1
            else:
                low = mid + 1

        return -1


if __name__ == "__main__":
    print Solution().findPeakElement([1, 2])
