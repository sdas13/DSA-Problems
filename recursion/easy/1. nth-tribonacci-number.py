"""
The Tribonacci sequence Tn is defined as follows:
T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.
Given n, return the value of Tn.

Input: n = 4
Output: 4
Explanation: T_3 = 0 + 1 + 1 = 2, T_4 = 1 + 1 + 2 = 4

Input: n = 25
Output: 1389537
"""


class Solution:
    def tribonacci(self, n: int) -> int:

        if n == 0: return 0
        if n == 1 or n == 2: return 1

        n0, n1, n2 = 0, 1, 1
        for i in range(3, n + 1):
            next_item = n0 + n1 + n2
            n0 = n1
            n1 = n2
            n2 = next_item

        return next_item

        # return self.tribonacci(n-1) + self.tribonacci(n - 2) + self.tribonacci(n - 3)


# print(Solution().tribonacci(0))
# print(Solution().tribonacci(1))
# print(Solution().tribonacci(2))
# print(Solution().tribonacci(3))
# print(Solution().tribonacci(4))
# print(Solution().tribonacci(25))
print(Solution().tribonacci(37))
