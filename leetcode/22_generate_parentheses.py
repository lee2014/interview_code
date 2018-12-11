#!/usr/bin/env python
# -*- coding: utf-8 -*-

__mtime__ = '2018/11/23'


# Run 28 ms
class Solution(object):
    def __init__(self):
        self.parenthesis = []

    def _genParenthesis(self, n, string, stack):
        stack_len = len(stack)
        if n == 0:
            self.parenthesis.append(string + ")" * len(stack))
        elif stack_len == 0:
            new_stack = list(stack)
            new_stack.append("(")
            self._genParenthesis(n - 1, string + "(", new_stack)
        else:
            new_stack = list(stack)
            new_stack.append("(")
            self._genParenthesis(n - 1, string + "(", new_stack)

            new_stack.pop()
            new_stack.pop()
            self._genParenthesis(n, string + ")", new_stack)

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.parenthesis = []
        self._genParenthesis(n, "", [])
        return self.parenthesis


if __name__ == '__main__':
    solution = Solution()
    solution.generateParenthesis(3)
    print solution.parenthesis
