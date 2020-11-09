"""
Given an array of integers, find if the array contains any duplicates.

Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

Input: [1,2,3,1]
Output: true

Input: [1,2,3,4]
Output: false

Input: [1,1,1,3,3,4,3,2,4,2]
Output: true
"""


class Solution:
    def containsDuplicate(self, nums: list) -> bool:
        # Using Map
        obj = {}
        for i in nums:
            if i in obj:
                return True
            else:
                obj[i] = 1

        return False

        # One-liner using set
        # s = set(nums)
        # return len(nums) != len(s)


# print(Solution().containsDuplicate([1,1]))
# print(Solution().containsDuplicate([1, 2, 3, 1]))
print(Solution().containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))
