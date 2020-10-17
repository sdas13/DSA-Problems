"""
Given an array of 2n integers, your task is to group these integers into n pairs of integer, say (a1, b1), (a2, b2), ..., (an, bn) which makes sum of min(ai, bi) for all i from 1 to n as large as possible.

Input: [1,4,3,2]

Output: 4
Explanation: n is 2, and the maximum sum of pairs is 4 = min(1, 2) + min(3, 4).
"""


class Solution:
    def arrayPairSum(self, nums: list) -> int:
        nums.sort()
        i = 0
        sum = 0
        while i < len(nums):
            sum += nums[i]
            i += 2

        return sum


# print(Solution().arrayPairSum([1, 4, 3, 2]))
# print(Solution().arrayPairSum([3, 9, 2, 4, 7, 3, 9, 1, 0, 3, 7, 5, 3, 9, 2, 3]))
print(Solution().arrayPairSum([3, 9, 2, -4, 7, -3, -9, 1, 0, 3, 7, -5, 3, 9, 2, 3]))
