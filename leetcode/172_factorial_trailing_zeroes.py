#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Given an integer n, return the number of trailing zeroes in n!.

Example 1:

Input: 3
Output: 0
Explanation: 3! = 6, no trailing zero.
Example 2:

Input: 5
Output: 1
Explanation: 5! = 120, one trailing zero.
Note: Your solution should be in logarithmic time complexity.
"""

__mtime__ = '2018/12/7'


# Run 28 ms
class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """

        zeroes = 0
        num = n / 5
        while num != 0:
            zeroes += num
            num /= 5

        return zeroes
