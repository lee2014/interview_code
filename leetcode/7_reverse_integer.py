#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:
    Input: 123
    Output: 321
    
Example 2:
    Input: -123
    Output: -321
    
Example 3:
    Input: 120
    Output: 21
"""
__mtime__ = '2018/11/22'


# Run 32ms
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        int_max = 2 ** 31 - 1
        int_min = 2 ** 31 * -1

        if not (int_min < x < int_max):
            return 0

        flag = 1 if x > 0 else -1
        abs_x = x if x > 0 else -x

        rev_s = reverse_str(str(abs_x))
        res_x = int(rev_s) * flag

        if int_min < res_x < int_max:
            return res_x
        else:
            return 0


def reverse_str(string):
    string = "".join(reversed(string))
    return string


if __name__ == "__main__":
    solution = Solution()

    print solution.reverse(123) == 321
    print solution.reverse(-123) == -321
    print solution.reverse(120) == 21
    print solution.reverse(0) == 0
    print solution.reverse(-1) == -1
