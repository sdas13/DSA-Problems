"""
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.


Input: nums = [1,3,5,6], target = 5
Output: 2

Input: nums = [1,3,5,6], target = 2
Output: 1

Input: nums = [1,3,5,6], target = 7
Output: 4

Input: nums = [1,3,5,6], target = 0
Output: 0
"""


class Solution:
    def searchInsert(self, nums: list, target: int) -> int:

        min_indx = 0
        max_indx = len(nums) - 1

        while min_indx <= max_indx:
            mid = (min_indx + max_indx) // 2
            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                max_indx = mid - 1
            else:
                min_indx = mid + 1

        return max_indx + 1


# print(Solution().searchInsert([1, 3, 5, 6], 5))
# print(Solution().searchInsert([1, 3, 5, 6], 1))
# print(Solution().searchInsert([1, 3, 5, 6], 2))
# print(Solution().searchInsert([1, 3, 5, 6], 4))
# print(Solution().searchInsert([1, 3, 5, 6], 7))
print(Solution().searchInsert([1, 3, 5, 6], 0))
