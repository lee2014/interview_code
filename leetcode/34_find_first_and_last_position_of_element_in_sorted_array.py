"""
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
"""


# Run 40 ms
class Solution(object):
    def __mid_search(self, first, last, nums, target):
        if first > last:
            return -1
        if nums[first] > target:
            return -1
        if nums[last] < target:
            return -1

        mid = (first + last) / 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            return self.__mid_search(first, mid- 1, nums, target)
        else:
            return self.__mid_search(mid + 1, last, nums, target)

    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        n = len(nums)
        init_index = self.__mid_search(0, n - 1, nums, target)
        min_idx = -1
        max_idx = -1

        index = init_index
        while index != -1:
            min_idx = index
            index = self.__mid_search(0, min_idx - 1, nums, target)

        index = init_index
        while index != -1:
            max_idx = index
            index = self.__mid_search(max_idx + 1, n - 1, nums, target)

        return [min_idx, max_idx]
