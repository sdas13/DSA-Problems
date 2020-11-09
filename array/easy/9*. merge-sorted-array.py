"""
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:

The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is equal to m + n) to hold additional elements from nums2.

Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]

"""


class Solution:
    def merge(self, nums1: list, m: int, nums2: list, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m - 1
        j = n - 1
        k = m + n - 1

        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                k -= 1
                i -= 1
            else:
                nums1[k] = nums2[j]
                k -= 1
                j -= 1

        while j >= 0:
            nums1[k] = nums2[j]
            k -= 1
            j -= 1

        return nums1


# print(Solution().merge([2, 2, 2, 0, 0, 0], 3, [1, 1, 1], 3))
# print(Solution().merge([1, 2, 0, 0], 2, [1, 2], 2))
# print(Solution().merge([1, 1, 1, 1, 1, 0, 0, 0], 5, [2, 2, 2], 3))
# print(Solution().merge([2, 2, 2, 0, 0, 0, 0, 0, ], 3, [1, 1, 1, 1, 1], 5))
print(Solution().merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3))
