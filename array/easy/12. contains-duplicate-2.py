"""
Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k.

https://leetcode.com/problems/contains-duplicate-ii/discuss/61375/Python-concise-solution-with-dictionary./395343

Input: nums = [1,2,3,1], k = 3
Output: true

Input: nums = [1,0,1,1], k = 1
Output: true

Input: nums = [1,2,3,1,2,3], k = 2
Output: false

"""


class Solution:
    def containsNearbyDuplicate(self, nums: list, k: int) -> bool:

        indices = {}

        for i, j in enumerate(nums):

            if j in indices:
                temp = indices[j]
                if abs(temp - i) <= k:
                    return True

            indices[j] = i

        return False


# print(Solution().containsNearbyDuplicate([1, 2, 3, 1], 3))
# print(Solution().containsNearbyDuplicate([1, 0, 1, 1], 1))
print(Solution().containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2))
