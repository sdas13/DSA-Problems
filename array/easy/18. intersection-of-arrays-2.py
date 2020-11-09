"""
Given two arrays, write a function to compute their intersection.

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
"""


class Solution:
    def intersect(self, nums1: list, nums2: list) -> list:
        count1 = {}
        res = []

        for i in nums1:
            # count1[i] = count1.get(i, 0) + 1

            if i in count1:
                count1[i] += 1
            else:
                count1[i] = 1

        for i in nums2:
            if i in count1 and count1[i] > 0:
                res.append(i)
                count1[i] -= 1

        return res


# print(Solution().intersect([1, 2, 2, 1], [2, 2]))
print(Solution().intersect([4, 9, 5], [9, 4, 9, 8, 4]))
