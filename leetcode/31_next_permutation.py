#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place and use only constant extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1

"""

__mtime__ = '2018/11/28'


# Run 32 ms
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

    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        def find_first_desc_elem(l):
            i = len(l) - 1

            while i > 0:
                if l[i] > l[i - 1]:
                    return i
                i -= 1

            return i

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

        first_idx = find_first_desc_elem(nums)

        if first_idx == 0:
            nums.reverse()
        else:
            second_idx = self.find_min_num_large_than_k(first_idx, len(nums) - 1, nums, nums[first_idx - 1])
            if second_idx == -1:
                second_idx = first_idx

            nums[first_idx - 1] = nums[first_idx - 1] ^ nums[second_idx]
            nums[second_idx] = nums[first_idx - 1] ^ nums[second_idx]
            nums[first_idx - 1] = nums[first_idx - 1] ^ nums[second_idx]

            quick_sort(nums, first_idx, len(nums) - 1)


if __name__ == "__main__":
    solution = Solution()
    test = [1, 2, 3]

    solution.nextPermutation(test)
    print test == [1, 3, 2]
    solution.nextPermutation(test)
    print test == [2, 1, 3]
    solution.nextPermutation(test)
    print test == [2, 3, 1]
    solution.nextPermutation(test)
    print test == [3, 1, 2]
    solution.nextPermutation(test)
    print test == [3, 2, 1]
    solution.nextPermutation(test)
    print test == [1, 2, 3]
