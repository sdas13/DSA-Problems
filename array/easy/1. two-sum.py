"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target

Input: nums = [2,7,11,15], target = 9
Output: [0,1]

Input: nums = [3,3], target = 6
Output: [0,1]
"""
class Solution:
    def twoSum(self, nums: list, target: int) -> list:
        map = {}
        for i, j in enumerate(nums):
            diff = target - j
            if diff in map:
                return [map[diff], i]
            else:
                map[j] = i


# print(Solution().twoSum([2, 7, 11, 15], 9))
# print(Solution().twoSum([3, 2, 4], 6))
print(Solution().twoSum([3, 3], 6))
