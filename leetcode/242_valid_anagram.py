#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?
"""

__mtime__ = '2018/12/8'


# Run 36 ms
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        if len(s) != len(t):
            return False

        alphabets = [0] * 26
        ord_a = ord('a')
        for i, c in enumerate(s):
            pos = ord(c) - ord_a
            alphabets[pos] += 1
            pos = ord(t[i]) - ord_a
            alphabets[pos] -= 1

        for i in range(26):
            if alphabets[i] != 0:
                return False
        return True
