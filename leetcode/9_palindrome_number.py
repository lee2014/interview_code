#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Example 1:
    Input: 121
    Output: true

Example 2:
    Input: -121
    Output: false
    Explanation: From left to right, it reads -121. 
                 From right to left, it becomes 121-. Therefore it is not a palindrome.
    
    
Example 3:
    Input: 10
    Output: false
    Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
    
Follow up:
    Coud you solve it without converting the integer to a string?
"""

__mtime__ = '2018/11/23'


# Run 144 ms
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        if x < 0:
            return False
        if x == 0:
            return True

        # the following code can be stead of return int(str(x)[::-1]) == x
        reversed_x = 0
        i = x
        while i != 0:
            reversed_x = reversed_x * 10 + i % 10
            i /= 10

        return reversed_x == x
