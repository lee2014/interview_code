#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

Example 1:

Input: s = "egg", t = "add"
Output: true
Example 2:

Input: s = "foo", t = "bar"
Output: false
Example 3:

Input: s = "paper", t = "title"
Output: true
Note:
You may assume both s and t have the same length.
"""

__mtime__ = '2018/12/26'


# Run 48 ms
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        s_map = {}
        s_list = []
        s_count = 0
        t_map = {}
        t_list = []
        t_count = 0

        for c in s:
            if c not in s_map:
                s_map[c] = s_count
                s_count += 1
            s_list.append(s_map[c])

        for c in t:
            if c not in t_map:
                t_map[c] = t_count
                t_count += 1
            t_list.append(t_map[c])

        return s_list == t_list
