#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
Note: You may assume the string contain only lowercase letters.
"""

__mtime__ = '2018/12/8'


# Run 108 ms
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """

        if s is None or s == "":
            return -1

        alphbets = [0] * 26
        ord_a = ord('a')
        for c in s:
            alphbets[ord(c) - ord_a] += 1

        index = -1
        for i, c in enumerate(s):
            if alphbets[ord(c) - ord_a] == 1:
                index = i
                break
        return index
