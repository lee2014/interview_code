#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""


The count-and-say sequence is the sequence of integers with the first five terms as following:

1.     1
2.     11
3.     21
4.     1211
5.     111221
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.

Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say sequence.

Note: Each term of the sequence of integers will be represented as a string.
"""

__mtime__ = '2018/11/28'


# Run 68 ms
class Solution(object):
    def __init__(self):
        self.cache = ["" for _ in range(30)]

        for i in range(30):
            if i == 0:
                self.cache[0] = "1"
            else:
                self.cache[i] = self.say(self.cache[i - 1])

    def say(self, last_say_str):
        next_str_n = ""
        last_char = None
        count = 0
        for c in last_say_str:
            if last_char is None:
                last_char = c
                count = 1
            elif last_char == c:
                count += 1
            else:
                next_str_n += str(count) + last_char
                last_char = c
                count = 1

        if last_char is not None:
            next_str_n += str(count) + last_char
        return next_str_n

    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """

        return self.cache[n - 1]
