"""
Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2.

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]

Input: numbers = [2,3,4], target = 6
Output: [1,3]

Input: numbers = [-1,0], target = -1
Output: [1,2]
"""


class Solution:
    def twoSum(self, numbers: list, target: int) -> list:

        i = 0
        j = len(numbers)-1
        while i < j:
            temp = numbers[i] + numbers[j]
            if temp == target:
                return [i+1, j+1]
            elif temp < target:
                i += 1
            else:
                j -= 1

        return -1


print(Solution().twoSum([2, 7, 8, 10, 11, 15], 9))
