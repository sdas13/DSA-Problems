"""
You have to find a permutation of the string where no letter is followed by another letter and no digit is followed by another digit. That is, no two adjacent characters have the same type.
Return the reformatted string or return an empty string if it is impossible to reformat the string.

https://leetcode.com/problems/reformat-the-string/discuss/586674/Python-Simple-solution
Input: s = "covid2019"
Output: "c2o0v1i9d"

Input: s = "abcd1"
Output: ""
"""


class Solution:
    def reformat(self, s: str) -> str:

        i = 0
        j = 1
        s = list(s)

        while i < len(s) and j < len(s):

            if abs(ord(s[i]) - ord(s[j])) < 40:
                j += 1
            else:
                s[i + 1], s[j] = s[j], s[i + 1]
                i += 2
                j += 1

        if j - i > 1:
            return ''
        if i == j - 1 and abs(ord(s[i]) - ord(s[i-1])) < 40:
            s = [s[-1]] + s[:-1]

        return ''.join(s)


# print(Solution().reformat('covid2019'))
# print(Solution().reformat('c2o0v1i9d'))
# print(Solution().reformat('co2vid019'))
# print(Solution().reformat('1234abcd'))
# print(Solution().reformat('12a13bcd'))
# print(Solution().reformat('abc1234'))
# print(Solution().reformat('abcd123'))
# print(Solution().reformat('abc123'))
# print(Solution().reformat('abcd12'))
# print(Solution().reformat('abcd'))
print(Solution().reformat('ab123'))
