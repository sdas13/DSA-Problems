"""
A good string is a string which doesn't have two adjacent characters s[i] and s[i + 1] where s[i] is a lower-case letter and s[i + 1] is the same letter but in upper-case or vice-versa.
To make the string good, you can choose two adjacent characters that make the string bad and remove them. You can keep doing this until the string becomes good.

https://leetcode.com/problems/make-the-string-great/discuss/780897/C%2B%2B-Brute-Force-%2B-Two-Pointers
https://leetcode.com/problems/make-the-string-great/discuss/781009/Java-Simple-Solution-using-Stack-Explained

Input: s = "leEeetcode"
Output: "leetcode"

Input: s = "abBAcC"
Output: ""
"abBAcC" --> "aAcC" --> "cC" --> ""

"""


class Solution:
    def makeGood(self, s: str) -> str:

        s = list(s)

        i = 0

        while i < len(s) - 1:

            if abs(ord(s[i]) - ord(s[i + 1])) == 32:
                s = s[:i] + s[i + 2:]
                if i > 0: i -= 1
            else:
                i += 1

        return ''.join(s)


# print(Solution().makeGood('leEeetcode'))
# print(Solution().makeGood('abBAcC'))
# print(Solution().makeGood('abBAcCxyz'))
print(Solution().makeGood('s'))
