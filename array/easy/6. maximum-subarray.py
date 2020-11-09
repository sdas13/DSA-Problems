"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum

# kadane algorithm

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6

Input: nums = [-2147483647]
Output: -2147483647
"""


class Solution:
    #kadane algorithm
    def maxSubArray(self, nums: list) -> int:
        i = 1
        max_till_now = nums[0]
        local_max = nums[0]
        while i < len(nums):
            current = nums[i]
            local_max = max(current, local_max + current)
            max_till_now = max(max_till_now, local_max)
            i += 1

        return max_till_now


# print(Solution().maxSubArray([-1]))
# print(Solution().maxSubArray([-2, 1]))
# print(Solution().maxSubArray([-2, 1, 2]))
# print(Solution().maxSubArray([-2, 1, 2, 3]))
# print(Solution().maxSubArray([-2, 1, -3, 4]))
print(Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
