#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Shuffle a set of numbers without duplicates.

Example:

// Init an array with set 1, 2, and 3.
int[] nums = {1,2,3};
Solution solution = new Solution(nums);

// Shuffle the array [1,2,3] and return its result. Any permutation of [1,2,3] must equally likely to be returned.
solution.shuffle();

// Resets the array back to its original configuration [1,2,3].
solution.reset();

// Returns the random shuffling of array [1,2,3].
solution.shuffle();
"""

__mtime__ = '2018/12/9'


class Solution(object):
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.origin = list(nums)
        self.compare_list = [1, -1]

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self.origin

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """

        def compare(item1, item2):
            import random
            return self.compare_list[random.randint(0, 1)]

        return sorted(self.origin, cmp=compare)


if __name__ == "__main__":
    # Your Solution object will be instantiated and called as such:
    nums = [1, 2, 3]
    obj = Solution(nums)
    print nums
    param_1 = obj.reset()
    print param_1
    param_2 = obj.shuffle()
    print param_2
