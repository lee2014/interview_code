#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Write a program that outputs the string representation of numbers from 1 to n.

But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”. For numbers which are multiples of both three and five output “FizzBuzz”.

Example:

n = 15,

Return:
[
    "1",
    "2",
    "Fizz",
    "4",
    "Buzz",
    "Fizz",
    "7",
    "8",
    "Fizz",
    "Buzz",
    "11",
    "Fizz",
    "13",
    "14",
    "FizzBuzz"
]
"""

__mtime__ = '2018/12/8'


# Run 76 ms
class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        result = []

        for i in range(n):
            output = ""
            if (i + 1) % 3 == 0:
                output += "Fizz"
            if (i + 1) % 5 == 0:
                output += "Buzz"
            if (i + 1) % 3 != 0 and (i + 1 ) % 5 != 0:
                output = str(i+1)
            result.append(output)

        return result
