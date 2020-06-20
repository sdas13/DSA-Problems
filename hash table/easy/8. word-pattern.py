"""
Given a pattern and a string s, find if s follows the same pattern. Here follow means a full match, such that there is a
bijection between a letter in pattern and a non-empty word in s.

https://leetcode.com/problems/word-pattern/solution/

Input: pattern = "abba", s = "dog cat cat dog" Output: true
Input: pattern = "abba", s = "dog cat cat fish" Output: false
Input: pattern = "aaaa", s = "dog cat cat dog" Output: false
"""

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        # instead of storing a:b and b:a, store a:0, b:0
        mapping1 = {}
        mapping2 = {}

        s = s.split()

        if len(s) != len(pattern):
            return False

        for i, j in enumerate(pattern):
            if (j in mapping1 and mapping1[j] != s[i]) or (s[i] in mapping2 and mapping2[s[i]] != j):
                return False
            mapping1[j] = s[i]
            mapping2[s[i]] = j

        return True


# Solution().wordPattern('abd', 'dog cat cat')
# Solution().wordPattern('abba', 'dog cat cat dog')
Solution().wordPattern('abc', 'b c a')
