"""
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
"""


class Solution:
    def moveZeroes(self, nums: list) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return nums

        i = 0
        j = 0
        while j < len(nums):

            if nums[i] == 0 and nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]

            if nums[i] != 0:
                i += 1

            j += 1

        return nums


# print(Solution().moveZeroes([1]))
# print(Solution().moveZeroes([1, 2, 3, 0, 0, 0]))
# print(Solution().moveZeroes([1, 0, 1]))
# print(Solution().moveZeroes([1, 1, 1, 0, 0, 0, 1, 1]))
# print(Solution().moveZeroes([0, 1]))
# print(Solution().moveZeroes([0, 1, 0, 0, 0, 0]))
print(Solution().moveZeroes([0, 1, 2, 4, 5]))
# print(Solution().moveZeroes([0, 1, 2, 0, 4, 5, 0]))
# print(Solution().moveZeroes([0, 1, 0, 3, 12]))
