"""
Given an array nums and a value val, remove all instances of that value in-place and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.

Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2]
Explanation: Your function should return length = 2, with the first two elements of nums being 2.
It doesn't matter what you leave beyond the returned length. For example if you return 2 with nums = [2,2,3,3] or nums = [2,3,0,0], your answer will be accepted.

Input: nums = [0,1,2,2,3,0,4,2], val = 2
Output: 5, nums = [0,1,4,0,3]
Explanation: Your function should return length = 5, with the first five elements of nums containing 0, 1, 3, 0, and 4. Note that the order of those five elements can be arbitrary. It doesn't matter what values are set beyond the returned length.
"""


class Solution:
    def removeElement(self, nums: list, val: int) -> int:
        i = 0
        j = len(nums) - 1

        while i < j:
            if nums[j] == val:
                j -= 1

            if nums[i] != val:
                i += 1

            if i > j:
                break

            if nums[i] == val and nums[j] != val:
                nums[i], nums[j] = nums[j], nums[i]
                j -= 1
                i += 1

        return len(nums) - nums.count(val)


# print(Solution().removeElement([], 2))
# print(Solution().removeElement([1], 2))
# print(Solution().removeElement([2,2,2], 2))
# print(Solution().removeElement([2, 1, 2, 2, 1, 2], 2))
# print(Solution().removeElement([1, 1, 1, 2, 2, 2], 2))
# print(Solution().removeElement([2, 2, 2, 1, 1, 1], 2))
# print(Solution().removeElement([3, 2, 2, 3], 3))
# print(Solution().removeElement([3, 2, 2, 3], 3))
# print(Solution().removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2))
