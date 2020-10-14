"""
Given a word, you need to judge whether the usage of capitals in it is right or not: like

All letters in this word are capitals, like "USA".
All letters in this word are not capitals, like "leetcode".
Only the first letter in this word is capital, like "Google".

Input: "USA"
Output: True

Input: "FlaG"
Output: False
"""


class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return word.capitalize() == word or word.isupper() or word.islower()


print(Solution().detectCapitalUse('USA'))
