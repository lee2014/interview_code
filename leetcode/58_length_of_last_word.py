#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

Example:

Input: "Hello World"
Output: 5
"""

__mtime__ = '2018/12/23'


class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """

        n = len(s)

        last_len = 0
        i = n - 1
        count_state = 0
        while i >= 0 and count_state != 2:
            if s[i] != ' ':
                last_len += 1
                count_state = 1
            elif s[i] == ' ' and count_state != 0:
                count_state = 2
            i -= 1

        return last_len
