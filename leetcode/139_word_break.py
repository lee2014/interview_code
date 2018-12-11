#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words,
determine if s can be segmented into a space-separated sequence of one or more dictionary words.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
             Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false
"""

__mtime__ = '2018/12/6'


class Solution(object):
    def is_prefix(self, string, pre_str):
        if len(string) < len(pre_str):
            return False
        else:
            for i, c in enumerate(pre_str):
                if c != string[i]:
                    return False
            return True

    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """

        if len(s) == 0:
            return True

        return reduce(
            (lambda x, y: x or y),
            [self.wordBreak(s[len(w):], wordDict) if self.is_prefix(s, w) else False for w in wordDict] + [False]
        )


if __name__ == "__main__":
    print Solution().wordBreak("leetcode", ["leet","code"])
