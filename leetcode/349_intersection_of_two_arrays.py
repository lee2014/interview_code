#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Note:

Each element in the result must be unique.
The result can be in any order.
"""

__mtime__ = '2018/12/24'


# Run 36 ms
class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        nums1.sort()
        nums2.sort()

        i = 0
        j = 0
        n1 = len(nums1)
        n2 = len(nums2)

        result = []
        while i < n1 and j < n2:
            if nums1[i] == nums2[j]:
                result.append(nums1[i])
                last_number = nums1[i]
                while i < n1 and nums1[i] == last_number:
                    i += 1
                while j < n2 and nums2[j] == last_number:
                    j += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                i += 1

        return result
