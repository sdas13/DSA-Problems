"""
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.​

Input: nums = [3,0,1]
Output: 2

Input: nums = [0,1]
Output: 2

Input: nums = [9,6,4,2,3,5,7,0,1]
Output: 8

Input: nums = [0]
Output: 1
"""


class Solution:
    def missingNumber(self, nums: list) -> int:

        actual_total = sum(nums)

        expected_total = len(nums)*(len(nums)+1)//2

        return expected_total-actual_total


# print(Solution().missingNumber([3, 0, 1]))
# print(Solution().missingNumber([0, 1]))
# print(Solution().missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]))
print(Solution().missingNumber([1]))
