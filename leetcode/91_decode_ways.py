#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given a non-empty string containing only digits, determine the total number of ways to decode it.

Example 1:

Input: "12"
Output: 2
Explanation: It could be decoded as "AB" (1 2) or "L" (12).
Example 2:

Input: "226"
Output: 3
Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
"""

__mtime__ = '2018/12/5'


# Run 24 ms
class Solution(object):
    def __init__(self):
        self.decode_num = [1, 1, 2]

    def decode_num_by_n(self, n):
        if n + 1 > len(self.decode_num):
            i = len(self.decode_num)
            while i <= n:
                self.decode_num.append(self.decode_num[i-1] + self.decode_num[i-2])
                i += 1
        return self.decode_num[n]

    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """

        decode_ways = 1
        curr_way = 0
        last_char = None

        for c in s:
            if curr_way == 0 and c == '0':
                return 0
            elif c == '0':
                decode_ways *= self.decode_num_by_n(curr_way - 1)
                curr_way = 0
            elif c == '1' or c == '2':
                curr_way += 1
            elif last_char == '2' and '3' <= c <= '6':
                decode_ways *= self.decode_num_by_n(curr_way + 1)
                curr_way = 0
            elif last_char == '2' and c > '6':
                decode_ways *= self.decode_num_by_n(curr_way)
                curr_way = 0
            elif last_char == '1' and c > '2':
                decode_ways *= self.decode_num_by_n(curr_way + 1)
                curr_way = 0
            else:
                curr_way = 0

            last_char = c

        if curr_way != 0:
            decode_ways *= self.decode_num_by_n(curr_way)

        return decode_ways
