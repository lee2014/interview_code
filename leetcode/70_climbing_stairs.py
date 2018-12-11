#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""


You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.

Example 1:

Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
"""

__mtime__ = '2018/12/8'


# Run 28 ms
class Solution(object):
    def __init__(self):
        self.steps = [1] * 100
        self.steps[0] = 0
        self.steps[1] = 1
        self.steps[2] = 2

        for i in range(97):
            self.steps[i+3] = self.steps[i+2] + self.steps[i+1]

    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

        return self.steps[n]

