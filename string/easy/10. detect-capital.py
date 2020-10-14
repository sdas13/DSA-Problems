"""
Given a word, you need to judge whether the usage of capitals in it is right or not: like

All letters in this word are capitals, like "USA".
All letters in this word are not capitals, like "leetcode".
Only the first letter in this word is capital, like "Google".

https://leetcode.com/problems/detect-capital/discuss/99248/3-Lines

Input: "USA"
Output: True

Input: "FlaG"
Output: False
"""


class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return word.capitalize() == word or word.isupper() or word.islower() # istitle()


print(Solution().detectCapitalUse('USA'))
