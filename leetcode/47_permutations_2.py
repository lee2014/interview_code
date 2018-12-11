#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Given a collection of numbers that might contain duplicates, return all possible unique permutations.

Example:

Input: [1,1,2]
Output:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]

"""

__mtime__ = '2018/11/28'


# Run 60ms
class Solution(object):
    def find_min_num_large_than_k(self, low, high, l, k):
        if low > high:
            return -1
        elif low == high and l[low] > k:
            return low
        elif low == high:
            return -1
        elif low == high - 1:
            if l[low] > k >= l[high]:
                return low
            elif l[high] > k:
                return high
            else:
                return -1
        else:
            mid = (low + high) / 2
            if l[mid] == k:
                return self.find_min_num_large_than_k(low, mid-1, l, k)
            elif k < l[mid]:
                return self.find_min_num_large_than_k(mid, high, l, k)
            else:
                return self.find_min_num_large_than_k(low, mid, l, k)

    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        def quick_sort(l, first, last):
            if first < last:
                split_point = partition(l, first, last)

                quick_sort(l, first, split_point - 1)
                quick_sort(l, split_point+1, last)

        def partition(l, first, last):
            target = l[first]

            low = first + 1
            high = last

            while low <= high:
                while low <= high and l[low] <= target:
                    low = low + 1

                while low <= high and l[high] >= target:
                    high = high - 1

                if low < high:
                    l[low] = l[low] ^ l[high]
                    l[high] = l[low] ^ l[high]
                    l[low] = l[low] ^ l[high]

            l[first] = l[high]
            l[high] = target

            return high

        def find_first_desc_elem(l):
            i = len(l) - 1

            while i > 0:
                if l[i] > l[i - 1]:
                    return i
                i -= 1

            return i

        numbers = sorted(nums)
        length = len(numbers)
        idx = find_first_desc_elem(numbers)
        lists = [list(numbers)]

        while idx != 0:
            second_idx = self.find_min_num_large_than_k(idx, length - 1, numbers, numbers[idx - 1])
            if second_idx == -1:
                second_idx = idx

            numbers[idx - 1] = numbers[idx - 1] ^ numbers[second_idx]
            numbers[second_idx] = numbers[idx - 1] ^ numbers[second_idx]
            numbers[idx - 1] = numbers[idx - 1] ^ numbers[second_idx]

            quick_sort(numbers, idx, length - 1)
            lists.append(list(numbers))

            idx = find_first_desc_elem(numbers)

        return lists
