"""
Given a non-empty array of non-negative integers nums, the degree of this array is defined as the maximum frequency of any one of its elements.
Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has the same degree as nums.

https://leetcode.com/problems/degree-of-an-array/discuss/124317/JavaC++Python-One-Pass-Solution

Input: nums = [1,2,2,3,1]
Output: 2
Explanation: The input array has a degree of 2 because both elements 1 and 2 appear twice.
Of the subarrays that have the same degree: [1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
The shortest length is 2. So return 2.

Input: nums = [1,2,2,3,1,4,2]
Output: 6
Explanation:  The degree is 3 because the element 2 is repeated 3 times.
So [2,2,3,1,4,2] is the shortest subarray, therefore returning 6.
"""


class Solution:
    def findShortestSubArray(self, nums: list) -> int:

        counts = {}
        indx_map = {}
        degree = 0
        min_subarr_len = len(nums)

        for j, i in enumerate(nums):
            counts[i] = counts.get(i, 0) + 1
            if i not in indx_map:
                indx_map[i] = [j, j, counts[i]]

            if counts[i] >= degree:
                degree = counts[i]
                indx_map[i][1] = j
                indx_map[i][2] = degree

        # degree = max(count.values())

        for i in indx_map:
            if indx_map[i][2] == degree:
                min_subarr_len = min(min_subarr_len, indx_map[i][1] - indx_map[i][0] + 1)

        return min_subarr_len


# print(Solution().findShortestSubArray([1, 2, 2, 3, 1]))
# print(Solution().findShortestSubArray([1, 2, 2, 3, 1, 4, 2]))
# print(Solution().findShortestSubArray([1, 2, 2, 3, 1, 2, 2, 2, 2]))
print(Solution().findShortestSubArray([1, 1, 2, 2, 2, 1]))
