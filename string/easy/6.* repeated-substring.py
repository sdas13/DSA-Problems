"""
Given a non-empty string check if it can be constructed by taking a substring of it and appending multiple copies of the substring together

Input: "abab"
Output: True

Input: "aba"
Output: False

Input: "abcabcabcabc"
Output: True

https://leetcode.com/problems/repeated-substring-pattern/discuss/?currentPage=1&orderBy=most_votes&query=

s=abcabc (2 abcs so 2 patterns)
s+s = abcabcabcabc (4 patterns)
remove 1 and last char (2 patterns gone so 2 patterns left)
bcabcabcab (last substr from string 1 and first substr from string 2. s is present )

s= abc (0 pattern)
s = abc+abc (2 patterns)
remove 1 and last (no pattern left)

"""


# start rotating each character of string one by one. If repeating pattern is there, after one pattern rotation, string will be same

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:

        if len(s) < 2: return False

        i = 1
        while i < (len(s) // 2) + 1:  # a pattern has to exist by half the length at max
            temp = s[i:] + s[:i]

            if temp == s:
                return True
            i += 1

        return False


# print(Solution().repeatedSubstringPattern('abcabc'))
# print(Solution().repeatedSubstringPattern('aba'))
# print(Solution().repeatedSubstringPattern('abcabcabcabc'))
# print(Solution().repeatedSubstringPattern('abac'))
# print(Solution().repeatedSubstringPattern('a'))
print(Solution().repeatedSubstringPattern('abaaba'))
