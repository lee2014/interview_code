#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Write a function that takes a string as input and returns the string reversed.

Example 1:

Input: "hello"
Output: "olleh"
Example 2:

Input: "A man, a plan, a canal: Panama"
Output: "amanaP :lanac a ,nalp a ,nam A"
"""

__mtime__ = '2018/12/8'


# Run 36 ms
class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """

        n = len(s)
        stack = [''] * n
        for i, c in enumerate(s):
            stack[n - i - 1] = c

        return "".join(stack)
