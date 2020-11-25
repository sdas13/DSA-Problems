"""
Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

must not use any built-in BigInteger library or convert the inputs to integer
"""


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        len1 = len(num1) - 1
        len2 = len(num2) - 1
        res = ''
        carry = 0

        while len1 >= 0 or len2 >= 0:
            n1 = int(num1[len1]) if len1 >= 0 else 0  # ord(num1[len1]) - ord('0')
            n2 = int(num2[len2]) if len2 >= 0 else 0
            temp = n1 + n2 + carry
            carry = temp // 10
            res = str(temp % 10) + res  # should have used array join instead of string concat
            len1 -= 1
            len2 -= 1

        return '1' + res if carry else res


# print(Solution().addStrings('123', '22'))
print(Solution().addStrings('9999', '9'))
