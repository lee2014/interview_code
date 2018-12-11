#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"
"""

__mtime__ = '2018/12/1'


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        new_s = "#" + '#'.join(s) + "#"






if __name__ == "__main__":
    print Solution().longestPalindrome("babad")
