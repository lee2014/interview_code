#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Given an array of strings, group anagrams together.

Example:
    Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
    Output:
        [
          ["ate","eat","tea"],
          ["nat","tan"],
          ["bat"]
        ]

Note:
    All inputs will be in lowercase.
    The order of your output does not matter.
"""

__mtime__ = '2018/11/26'


# Run 144ms
class Solution(object):
    def _hash(self, s):
        return "".join(sorted(s))

    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        result = {}

        for s in strs:
            hsh_code = self._hash(s)
            if hsh_code not in result:
                result[hsh_code] = [s]
            else:
                result[hsh_code].append(s)

        return result.values()
