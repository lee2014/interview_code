#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z.
"""

__mtime__ = '2018/11/22'


# Run 24 ms
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        if len(strs) == 0:
            return ""

        min_len = min([len(x) for x in strs])

        i = 0
        flag = True
        while i < min_len and flag:
            target = strs[0][i]
            for string in strs:
                if string[i] != target:
                    flag = False
                    break
            if flag:
                i += 1

        return strs[0][:i]


if __name__ == "__main__":
    solution = Solution()

    print solution.longestCommonPrefix(["flower", "flow", "flight"]) == "fl"
    print solution.longestCommonPrefix(["dog", "racecar", "car"]) == ""
