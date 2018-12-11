#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:
    Input: "()"
    Output: true

Example 2:
    Input: "()[]{}"
    Output: true

Example 3:
    Input: "(]"
    Output: false

Example 4:
    Input: "([)]"
    Output: false

Example 5:
    Input: "{[]}"
    Output: true
"""
__mtime__ = '2018/11/23'


# Run 20ms
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        bracket_stack = []

        for c in s:
            if c == '(':
                bracket_stack.append('(')
            elif c == '[':
                bracket_stack.append('[')
            elif c == '{':
                bracket_stack.append('{')
            elif c == ')':
                if len(bracket_stack) == 0 or bracket_stack[-1] != '(':
                    return False
                else:
                    bracket_stack.pop()
            elif c == ']':
                if len(bracket_stack) == 0 or bracket_stack[-1] != '[':
                    return False
                else:
                    bracket_stack.pop()
            elif c == '}':
                if len(bracket_stack) == 0 or bracket_stack[-1] != '{':
                    return False
                else:
                    bracket_stack.pop()
            else:
                pass

        return len(bracket_stack) == 0
