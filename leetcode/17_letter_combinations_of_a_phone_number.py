#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Given a string containing digits from 2-9 inclusive,
return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.
Note that 1 does not map to any letters.

Example:

Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
Note:

Although the above answer is in lexicographical order, your answer could be in any order you want.
"""

__mtime__ = '2018/12/9'


# Run 20 ms
class Solution(object):
    def __init__(self):
        self.mapping = {
            "1": [""],
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }

    def cartesian(self, list1, list2):
        list3 = []
        for i in list1:
            for j in list2:
                list3.append(i+j)
        return list3

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """

        if len(digits) == 0:
            return []

        result = [""]
        for digit in digits:
            result = self.cartesian(result, self.mapping[digit])
        return result

