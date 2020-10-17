"""
Given a non-empty array of digits representing a non-negative integer, increment one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contains a single digit.

Input: digits = [1,2,3]
Output: [1,2,4]

Input: digits = [9]
Output: [1,0]
"""


class Solution:
    def plusOne(self, digits: list) -> list:

        i = len(digits) - 1

        while i > -1:
            if digits[i] < 9:
                digits[i] += 1
                return digits
            else:
                digits[i] = 0
                i -= 1

        return [1] + digits


# print(Solution().plusOne([1, 2, 3]))
# print(Solution().plusOne([4, 3, 2, 1]))
# print(Solution().plusOne([0]))
print(Solution().plusOne([9, 9, 9]))
# print(Solution().plusOne([8, 9, 9, 9]))
