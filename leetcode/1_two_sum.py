"""
Given an array of integers,
return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution,
and you may not use the same element twice.

Example:
    Given nums = [2, 7, 11, 15], target = 9,
    Because nums[0] + nums[1] = 2 + 7 = 9,
    return [0, 1].
"""

__author__ = "Chengli"


class Solution(object):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """

    # Run 3080 ms
    def two_sum_1(self, nums, target):
        for idx, num in enumerate(nums):
            half_target = target - num
            for left_idx, left_num in enumerate(nums[idx + 1:]):
                if half_target == left_num:
                    return [idx, left_idx + idx + 1]

    # Run 984 ms
    def two_sum_2(self, nums, target):
        for idx, num in enumerate(nums):
            if (target - num) in nums[idx + 1:]:
                return [
                    nums.index(num),
                    nums[idx + 1:].index(target - num) + idx + 1
                ]

    # Run 22ms
    def two_sum_3(self, nums, target):
        sorted_nums = sorted(nums)

        for idx, num in enumerate(sorted_nums):
            if target - num in sorted_nums[idx + 1:]:
                first_idx = nums.index(num)
                if target - num != num:
                    second_idx = nums.index(target - num)
                else:
                    second_idx = nums[first_idx + 1:].index(target - num) + first_idx + 1
                return [first_idx, second_idx]
