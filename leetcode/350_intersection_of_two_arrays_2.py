#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Note:

Each element in the result should appear as many times as it shows in both arrays.
The result can be in any order.
Follow up:

What if the given array is already sorted? How would you optimize your algorithm?
What if nums1's size is small compared to nums2's size? Which algorithm is better?
What if elements of nums2 are stored on disk,
and the memory is limited such that you cannot load all elements into the memory at once?
"""

__mtime__ = '2018/12/8'


# Run 32ms
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        len_1 = len(nums1)
        len_2 = len(nums2)

        if len_1 == 0 or len_2 == 0:
            return []

        sort_nums1 = sorted(nums1)
        sort_nums2 = sorted(nums2)

        i = 0
        j = 0
        intersection = []
        while i < len_1 and j < len_2:
            if sort_nums1[i] == sort_nums2[j]:
                intersection.append(sort_nums1[i])
                i += 1
                j += 1
            elif sort_nums1[i] > sort_nums2[j]:
                j += 1
            else:
                i += 1

        return intersection
