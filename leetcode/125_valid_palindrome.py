#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false
"""

__mtime__ = '2018/12/6'


class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        def is_alph_char(c):
            return 'a' <= c <= 'z' or 'A' <= c <= 'Z' or '0' <= c <= '9'

        def compare_ignore_case(c1, c2):
            return c1.lower() == c2.lower()

        i = 0
        j = len(s) - 1
        while i < j:
            # find i
            while i < j and not is_alph_char(s[i]):
                i += 1

            # find j
            while i < j and not is_alph_char(s[j]):
                j -= 1

            if i < j:
                result = compare_ignore_case(s[i], s[j])
                i += 1
                j -= 1
                if not result:
                    return False

        return True


if __name__ == "__main__":
    print Solution().isPalindrome("9;8'4P?X:1Q8`dOfJuJXD6FF,8;`Y4! YBy'Wb:ll;;`;\"JI0c2uvD':!LAk:s\"!'0.!2B55.T1VI?00Du?1,l``RFsc?Y?9vD5 K'3'1b!N8hn:'l. R:9:o`m1r.M2mrJ?`Wjv1`G6i6G`1vjW`?Jrm2M.r1m`o:::R .l':nh8N!b1'3'K 5Dv9?Y?csFR``l,1?uD00?IV1T.55B2!.0'!\"s:kAL!:'Dvu2c0IJ\";`;;ll9bW'yBY !4Y`;8,FF6DXJuJfOd`8Q1:X?P4'8;9")
