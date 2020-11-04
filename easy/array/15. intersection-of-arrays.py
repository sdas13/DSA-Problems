"""
Given two arrays, write a function to compute their intersection.

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
"""


class Solution:
    def intersection(self, nums1: list, nums2: list) -> list:


        nums1_set = set(nums1)
        nums2_set = set(nums2)

        return nums1_set & nums2_set


# print(Solution().intersection([1, 2, 2, 1], [2, 2]))
print(Solution().intersection([4, 9, 5], [9, 4, 9, 8, 4]))
