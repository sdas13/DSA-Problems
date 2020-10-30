"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6

Input: nums = [-2147483647]
Output: -2147483647
"""


class Solution:
    def maxSubArray(self, nums: list) -> int:
        if len(nums) == 1:
            return nums[0]





# print(Solution().maxSubArray([-2, 1]))
# print(Solution().maxSubArray([-2, 1, 2]))
# print(Solution().maxSubArray([-2, 1, 2, 3]))


print(Solution().maxSubArray([-2, 1, -3, 4]))
# print(Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])


