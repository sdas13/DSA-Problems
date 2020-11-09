"""
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times

Input: [3,2,3]
Output: 3

Input: [2,2,1,1,1,2,2]
Output: 2

https://leetcode.com/problems/majority-element/solution/

"""


class Solution:
    def majorityElement(self, nums: list) -> int:

        if len(nums) == 1:
            return nums[0]

        map = {}
        nums_len = len(nums) / 2
        for i in nums:
            try:
                map[i] += 1
                if map[i] > nums_len:
                    return i
            except KeyError:
                map[i] = 1


# print(Solution().majorityElement([3, 2, 3]))
# print(Solution().majorityElement([2, 2, 1, 1, 1, 2, 2]))
print(Solution().majorityElement([1]))
