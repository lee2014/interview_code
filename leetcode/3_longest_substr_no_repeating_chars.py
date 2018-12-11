#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Given a string, find the length of the longest substring without repeating characters.

Example 1:
    Input: "abcabcbb"
    Output: 3 
    Explanation: The answer is "abc", with the length of 3. 
    
Example 2:
    Input: "bbbbb"
    Output: 1
    Explanation: The answer is "b", with the length of 1.
    
Example 3:
    Input: "pwwkew"
    Output: 3
    Explanation: The answer is "wke", with the length of 3. 

Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""

__mtime__ = '2018/11/22'


# Run 64ms
class Solution(object):

    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        str_len = len(s)

        hash_char = dict((key, 0) for key in s)
        max_len = 0

        i = 0
        j = 0

        while i <= str_len - 1 and j <= str_len - 1:
            if hash_char[s[j]] == 0:
                hash_char[s[j]] = 1
                max_len = j - i + 1 if j - i + 1 > max_len else max_len
                j += 1
            elif i == j:
                hash_char[s[j]] = 0
                i += 1
                j += 1
                hash_char[s[j]] = 1
            else:
                hash_char[s[i]] = 0
                i += 1

        return max_len


if __name__ == "__main__":
    solution = Solution()

    print solution.lengthOfLongestSubstring("abcabcbb")
    print solution.lengthOfLongestSubstring("bbbbb")
    print solution.lengthOfLongestSubstring("pwwkew")
    print solution.lengthOfLongestSubstring("abcadabac")
    print solution.lengthOfLongestSubstring("")
    print solution.lengthOfLongestSubstring("a")

