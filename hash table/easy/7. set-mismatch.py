"""
In set S, one of the numbers in the set got duplicated to another number in the set, which results in repetition of one number
and loss of another number.find the number occurs twice and then find the number that is missing.
Return them in the form of an array

XoR: https://leetcode.com/problems/set-mismatch/solution/
https://leetcode.com/problems/set-mismatch/discuss/105558/Oneliner-Python

Input: nums = [1,2,2,4]
Output: [2,3]
"""


class Solution:
    def findErrorNums(self, nums: list) -> list:
        num_list = [0] * ((len(nums)) + 1)

        for i in nums:
            num_list[i] += 1

        for i in range(1, len(num_list)):

            if num_list[i] == 0:
                missing = i

            if num_list[i] == 2:
                dup = i

        return [dup, missing]


# print(Solution().findErrorNums([1, 2, 2, 4]))
# print(Solution().findErrorNums([1, 1]))
print(Solution().findErrorNums([2, 2]))
