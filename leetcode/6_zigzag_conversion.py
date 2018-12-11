#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:

P     I    N
A   L S  I G
Y A   H R
P     I
"""

__mtime__ = '2018/12/1'


# Run 64 ms
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """

        if numRows == 1:
            return s

        T = 2 * (numRows - 1)

        s_len = len(s)
        new_str = [""] * s_len
        cycle = s_len / T + 1

        index = 0
        for i in range(numRows):
            if i == 0 or i == numRows - 1:
                for c in range(cycle):
                    if c * T + i < s_len:
                        new_str[index] = s[c*T + i]
                        index += 1
                    else:
                        break
            else:
                for c in range(cycle):
                    if c * T + i < s_len:
                        new_str[index] = s[c*T + i]
                        index += 1
                    if c * T + T - i < s_len:
                        new_str[index] = s[c * T + T - i]
                        index += 1

        return "".join(new_str)


if __name__ == "__main__":
    print Solution().convert("PAYPALISHIRING", 3)
