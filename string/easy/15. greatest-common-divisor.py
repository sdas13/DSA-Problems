"""
Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2. we say "t divides s"
if and only if s = t + ... + t  (t concatenated with itself 1 or more times)

https://leetcode.com/problems/greatest-common-divisor-of-strings/discuss/516621/Java-clean-solution-(0-ms)-100
Explanation - s1+s2 == s2+s1 if & only if s1 is a multiple of s2 or vice-versa
e.g. s1=abcabc, s2=abc, then s1+s2 = abcabcabc = s2+s1

Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"

Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"

Input: str1 = "ABCDEF", str2 = "ABC"
Output: ""
"""


class Solution:

    def gcd(self, a, b):
        if b == 0:
            return a
        return self.gcd(b, a % b)

    def gcdOfStrings(self, str1: str, str2: str) -> str:

        s1_set = set(str1)
        s2_set = set(str2)

        if s1_set == s2_set:
            len_1 = len(str1)
            len_2 = len(str2)
            gcd = self.gcd(len_1, len_2)
            if not (str1[:gcd] * (len_1 // gcd) == str1 and str2[:gcd] * (len_2 // gcd) == str2):
                return ""

            return str1[:gcd]

        return ""


print(Solution().gcdOfStrings('ABCABC', 'ABC'))
print(Solution().gcdOfStrings('ABABAB', 'ABAB'))
print(Solution().gcdOfStrings('LEFT', 'CODE'))
print(Solution().gcdOfStrings('ABCDEF', 'ABC'))
print(Solution().gcdOfStrings('ABCABCABC', 'ABCAA'))
