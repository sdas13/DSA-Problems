"""
Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.
Each letter in the magazine string can only be used once in your ransom note.

https://leetcode.com/problems/ransom-note/discuss/85757/pythonset()count()
https://leetcode.com/problems/ransom-note/discuss/85837/O(m%2Bn)-one-liner-Python

Input: ransomNote = "a", magazine = "b"
Output: false

Input: ransomNote = "aa", magazine = "ab"
Output: false

Input: ransomNote = "aa", magazine = "aab"
Output: true
"""


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        letters = {}
        for i in magazine:
            letters[i] = letters.get(i, 0) + 1

        for i in ransomNote:
            if not letters.get(i, 0):
                return False
            letters[i] -= 1

        return True


# print(Solution().canConstruct('a', 'b'))
# print(Solution().canConstruct('aa', 'ab'))
print(Solution().canConstruct('aa', 'aab'))
