#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 
    ...
Example 1:

Input: "A"
Output: 1
Example 2:

Input: "AB"
Output: 28
Example 3:

Input: "ZY"
Output: 701
"""

__mtime__ = '2018/12/7'


# Run 32 ms
class Solution(object):
    def __init__(self):
        self.mapping = dict([(chr(ord('A') + i), i + 1) for i in range(26)])

    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """

        num = 0
        for c in s:
            num = num * 26 + self.mapping[c]
        return num
