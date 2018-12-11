#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), 
design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

Example 1:

Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.
Example 2:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
"""

__mtime__ = '2018/12/6'


# Run 32 ms
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        min_prices = list(prices)
        profits = []

        for i, p in enumerate(prices):
            if i != 0:
                min_prices[i] = min([min_prices[i-1], p])
            profits.append(p - min_prices[i])

        profits.append(0)
        max_profit = max(profits)

        return max_profit
