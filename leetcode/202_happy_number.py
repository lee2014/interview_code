#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process:
Starting with any positive integer, replace the number by the sum of the squares of its digits,
and repeat the process until the number equals 1 (where it will stay),
or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy numbers.

Example: 

Input: 19
Output: true
Explanation: 
1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1
"""

__mtime__ = '2018/12/8'


# Run 24 ms
class Solution(object):
    def __init__(self):
        self.num_compute = {}
        self.happy_nums = {}

    def compute(self, n):
        if n not in self.num_compute:
            result = 0
            while n != 0:
                digit = n % 10
                result += digit * digit
                n = n / 10
            self.num_compute[n] = result
        return self.num_compute[n]

    def is_already_happy(self, n):
        return n in self.happy_nums

    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """

        my_map = {}
        num = n
        while num != 1 and num not in my_map:
            if self.is_already_happy(num):
                for key in my_map:
                    self.happy_nums[key] = 1
                return True
            new_n = self.compute(num)
            my_map[num] = new_n
            num = new_n

        if num == 1:
            for key in my_map:
                self.happy_nums[key] = 1
            return True
        else:
            return False


if __name__ == "__main__":
    solution = Solution()
    print solution.isHappy(2)
