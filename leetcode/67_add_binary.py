#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
"""

__mtime__ = '2018/12/23'


# Run 48 ms
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """

        a_n = len(a)
        b_n = len(b)
        bits = []

        i = a_n - 1
        j = b_n - 1
        carry = 0
        while i >= 0 or j >= 0:
            if i < 0:
                res = (int(b[j]) + carry) % 2
                carry = (int(b[j]) + carry) / 2
                j -= 1
            elif j < 0:
                res = (int(a[i]) + carry) % 2
                carry = (int(a[i]) + carry) / 2
                i -= 1
            else:
                res = (int(a[i]) + int(b[j]) + carry) % 2
                carry = (int(a[i]) + int(b[j]) + carry) / 2
                i -= 1
                j -= 1
            bits.append(str(res))

        if carry == 1:
            bits.append("1")

        while len(bits) > 1 and bits[-1] == '0':
            bits.pop()

        return "".join([bit for bit in reversed(bits)])
