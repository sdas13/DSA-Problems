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

        max_count = 0
        counts = {}

        # counts = collections.Counter(nums)
        # for i in nums:
        #     if i + 1 in counts:
        #         max_count = max(max_count, counts[i] + counts[i + 1])

        for i in nums:
            counts[i] = counts.get(i, 0) + 1
            if i + 1 in counts:
                max_count = max(max_count, counts[i] + counts[i + 1])

            if i - 1 in counts:
                max_count = max(max_count, counts[i] + counts[i - 1])

        return max_count


print(Solution().findLHS([1, 3, 2, 2, 5, 2, 3, 7]))
# print(Solution().findLHS([1, 1, 1, 1]))
