#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Implement atoi which converts a string to an integer.
The function first discards as many whitespace characters as necessary until the first non-whitespace character is found.
Then, starting from this character,
takes an optional initial plus or minus sign followed by as many numerical digits as possible,
and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number,
which are ignored and have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number,
or if no such sequence exists because either str is empty or it contains only whitespace characters,
no conversion is performed.

If no valid conversion could be performed, a zero value is returned.

Note:

Only the space character ' ' is considered as whitespace character.
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range:
[−2^31,  2^31 − 1].
If the numerical value is out of the range of representable values, INT_MAX (2^31 − 1) or INT_MIN (−2^31) is returned.

Example 1:
    Input: "42"
    Output: 42

Example 2:
    Input: "   -42"
    Output: -42
    Explanation: The first non-whitespace character is '-', which is the minus sign.
                 Then take as many numerical digits as possible, which gets 42.

Example 3:
    Input: "4193 with words"
    Output: 4193
    Explanation: Conversion stops at digit '3' as the next character is not a numerical digit.

Example 4:
    Input: "words and 987"
    Output: 0
    Explanation: The first non-whitespace character is 'w', which is not a numerical 
                 digit or a +/- sign. Therefore no valid conversion could be performed.

Example 5:
    Input: "-91283472332"
    Output: -2147483648
    Explanation: The number "-91283472332" is out of the range of a 32-bit signed integer.
                 Thefore INT_MIN (−231) is returned.
"""

__mtime__ = '2018/11/23'


# Run 36 ms
class Solution(object):
    def __init__(self):
        self.INT_MIN = 2 ** 31 * -1
        self.INT_MAX = 2 ** 31 - 1

        self.INIT = 0
        self.SIGN = 1
        self.NUMBER = 2
        self.ILLEGAL = 3


    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """

        state = self.INIT
        sign = 1
        i = 0
        length = len(str)
        result = 0
        while state != self.ILLEGAL and i < length:
            if state == self.INIT and str[i] == ' ':
                pass
            elif state == self.INIT and str[i] == '-':
                sign = -1
                state = self.NUMBER
            elif state == self.INIT and str[i] == '+':
                state = self.NUMBER
            elif state == self.INIT and '0' <= str[i] <= '9':
                state = self.NUMBER
                result = int(str[i])
            elif state == self.INIT:
                state = self.ILLEGAL
            elif state == self.NUMBER and '0' <= str[i] <= '9':
                state = self.NUMBER
                result = result * 10 + int(str[i])
            elif state == self.NUMBER:
                state = self.ILLEGAL

            i += 1

        result *= sign
        if self.INT_MIN <= result <= self.INT_MAX:
            return result
        if result < self.INT_MIN:
            return self.INT_MIN
        else:
            return self.INT_MAX


if __name__ == "__main__":
    solution = Solution()

    print solution.myAtoi(" -42") == -42
