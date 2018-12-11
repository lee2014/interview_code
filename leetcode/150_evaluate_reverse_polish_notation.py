#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each operand may be an integer or another expression.

Note:

Division between two integers should truncate toward zero.
The given RPN expression is always valid. That means the expression would always evaluate to a result and there won't be any divide by zero operation.
Example 1:

Input: ["2", "1", "+", "3", "*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9
Example 2:

Input: ["4", "13", "5", "/", "+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6
Example 3:

Input: ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
Output: 22
Explanation: 
  ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22
"""

__mtime__ = '2018/12/6'


# Run 44 ms
class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """

        def hash_func(op, a, b):
            if op == '+':
                return a + b
            elif op == '-':
                return a - b
            elif op == '*':
                return a * b
            else:
                return int(float(a) / b)

        stack = []

        for token in tokens:
            if len(stack) == 0:
                stack.append(token)
            elif token in ["+", "-", "*", "/"]:
                op2 = stack.pop()
                op1 = stack.pop()
                result = hash_func(token, int(op1), int(op2))
                stack.append(result)
                # print "%(result)s = %(op1)s %(token)s %(op2)s" % (locals())
            else:
                stack.append(token)

        return int(stack[0])


if __name__ == "__main__":
    Solution().evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"])
