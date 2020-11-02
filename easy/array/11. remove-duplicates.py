"""
Given a sorted array nums, remove the duplicates in-place such that each element appears only once and returns the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Input: nums = [1,1,2]
Output: 2, nums = [1,2]
Explanation: Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively. It doesn't matter what you leave beyond the returned length.

Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4]
Explanation: Your function should return length = 5, with the first five elements of nums being modified to 0, 1, 2, 3, and 4 respectively. It doesn't matter what values are set beyond the returned length.
"""


class Solution:
    def removeDuplicates(self, nums: list) -> int:
        j = 0

        for i in nums:

            if i != nums[j]:
                j += 1
                nums[j] = i

        return j+1


# print(Solution().removeDuplicates([1]))
# print(Solution().removeDuplicates([1, 2]))
# print(Solution().removeDuplicates([1, 2, 3, 4, 5]))
# print(Solution().removeDuplicates([1,1, 2, 3, 4, 5]))
# print(Solution().removeDuplicates([1, 1, 2]))
print(Solution().removeDuplicates([0, 0, 0, 0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
