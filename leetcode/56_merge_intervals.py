"""
Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
"""


# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e


# Run 80 ms
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """

        def compare(item1, item2):
            if item1.start < item2.start:
                return -1
            elif item1.start > item2.start:
                return 1
            elif item1.end < item2.end:
                return -1
            elif item1.end > item2.end:
                return 1
            else:
                return 0

        intervals.sort(cmp=compare)
        merge_interval = []

        for interval in intervals:
            if len(merge_interval) == 0:
                merge_interval.append(interval)
            else:
                last_interval = merge_interval[-1]
                if last_interval.start == interval.start:
                    last_interval.end = max([last_interval.end, interval.end])
                elif last_interval.end == interval.start:
                    last_interval.end = interval.end
                elif last_interval.end < interval.start:
                    merge_interval.append(interval)
                elif last_interval.end > interval.start:
                    last_interval.end = max([last_interval.end, interval.end])

        return merge_interval
