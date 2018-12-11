#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive),
prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.

Example 1:

Input: [1,3,4,2,2]
Output: 2
Example 2:

Input: [3,1,3,4,2]
Output: 3
Note:

You must not modify the array (assume the array is read only).
You must use only constant, O(1) extra space.
Your runtime complexity should be less than O(n2).
There is only one duplicate number in the array, but it could be repeated more than once.
"""

__mtime__ = '2018/12/10'


# Run 24 ms
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        """
        Define the following variables:
            1) x is the steps of first pointer;
            2) So, 2x is the steps of second pointer;
            3) d is the distance between head of list and head of cycle-list;
            4) k is the length of cycle-list;
            5) m is the distance between first pointer and head of cycle-list;
        
        For example:
                        first_pointer
                            |
                            v
        1 -> 2 -> 3 -> 5 -> 6 <- second_pointer   
                  ^         |
                  |         v
                  9 -> 8 -> 7
                  
        
        Move first_pointer by one step and second_pointer by two steps.
        When first_pointer meets second_pointer at fist time, the following formulas are sound:
            x = d + m + a*k
            2x = d + m + b*k
        
        So, 2*(d + m + a*k) == d + m + b*k
        And then, d + m = (b - 2*a)*k
        
        If we move the head_pointer and first_pointer by d steps, they will meet each other in the head of cycle-list.
        """

        head = 0
        first_p = nums[head]
        second_p = nums[nums[head]]
        while first_p != second_p:
            first_p = nums[first_p]
            second_p = nums[nums[second_p]]

        second_p = head
        while first_p != second_p:
            first_p = nums[first_p]
            second_p = nums[second_p]
        return first_p
