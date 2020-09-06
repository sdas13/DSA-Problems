"""
A good string is a string which doesn't have two adjacent characters s[i] and s[i + 1] where s[i] is a lower-case letter and s[i + 1] is the same letter but in upper-case or vice-versa.
To make the string good, you can choose two adjacent characters that make the string bad and remove them. You can keep doing this until the string becomes good.

Input: s = "leEeetcode"
Output: "leetcode"

Input: s = "abBAcC"
Output: ""
"abBAcC" --> "aAcC" --> "cC" --> ""

"""


class Solution:
    def makeGood(self, s: str) -> str:
        pass


print(Solution().makeGood('leEeetcode'))