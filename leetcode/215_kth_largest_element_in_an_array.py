#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Example 1:

Input: [3,2,1,5,6,4] and k = 2
Output: 5
Example 2:

Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4
"""
import heapq

__mtime__ = '2018/12/11'


# Run 68 ms
class Solution(object):
    class TopKHeap(object):
        def __init__(self, k):
            self.k = k
            self.data = []

        def push(self, elem):
            if len(self.data) < self.k:
                heapq.heappush(self.data, elem)
            else:
                topk_small = self.data[0]
                if elem > topk_small:
                    heapq.heapreplace(self.data, elem)

        def topk(self):
            return [x for x in [heapq.heappop(self.data) for x in xrange(len(self.data))]]

    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        top_k = self.TopKHeap(k)
        for num in nums:
            top_k.push(num)

        return top_k.topk()[0]


if __name__ == "__main__":
    solution = Solution()
    print solution.findKthLargest([3, 2, 1, 5, 6, 4], 2)
