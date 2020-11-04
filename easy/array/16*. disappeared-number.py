"""
Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/discuss/344583/Python%3A-O(1)-space-solution

Input:
[4,3,2,7,8,2,3,1]

Output:
[5,6]

"""


class Solution:
    def findDisappearedNumbers(self, nums: list) -> list:

        i = 1
        num_s = set(nums)
        res = []

        while i <= len(nums):
            if i not in num_s:
                res.append(i)

            i += 1

        return res


print(Solution().findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1]))
