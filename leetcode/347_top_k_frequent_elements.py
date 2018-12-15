#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Given a non-empty array of integers, return the k most frequent elements.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
Note:

You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
"""

__mtime__ = '2018/12/15'


# Run 64 ms
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        nums.sort()
        new_nums = []
        last_num = None
        count = 0
        for num in nums:
            if last_num is None:
                last_num = num
                count = 1
            elif last_num != num:
                new_nums.append([last_num, count])
                last_num = num
                count = 1
            else:
                count += 1

        new_nums.append([last_num, count])

        new_nums.sort(key=lambda i: i[1], reverse=True)
        return [item[0] for item in new_nums[:k]]

