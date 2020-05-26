"""
We define a harmonious array as an array where the difference between its maximum value and its minimum value is exactly 1. Given an integer array nums, return the length of its longest harmonious subsequence among all its possible subsequences.
A subsequence of array is a sequence that can be derived from the array by deleting some or no elements without changing the order of the remaining elements.

Input: nums = [1,3,2,2,5,2,3,7]
Output: 5 Explanation: The longest harmonious subsequence is [3,2,2,2,3].

Input: nums = [1,2,3,4]
Output: 2

Input: nums = [1,1,1,1]
Output: 0
"""

import collections


class Solution:
    def findLHS(self, nums: list) -> int:

        pass


print(Solution().findLHS([1, 3, 2, 2, 5, 2, 3, 7]))
# print(Solution().findLHS([1, 1, 1, 1]))
