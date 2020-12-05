"""
Write a function to find the longest common prefix string amongst an array of strings. If there is no common prefix, return an empty string ""

https://leetcode.com/problems/longest-common-prefix/solution/

Input: strs = ["flower","flow","flight"]
Output: "fl"

Input: strs = ["dog","racecar","car"]
Output: ""
"""


class Solution:
    def longestCommonPrefix(self, strs: list) -> str:
        if not strs: return ""

        common_str = strs[0]

        for i in range(1, len(strs)):

            j = 0

            while j < min(len(common_str), len(strs[i])):
                if common_str[j] != strs[i][j]:
                    break

                j += 1

            common_str = common_str[:j]

        return common_str


# print(Solution().longestCommonPrefix(["flower", "flow"]))
# print(Solution().longestCommonPrefix(["flower", "flow", "flight"]))
# print(Solution().longestCommonPrefix(["flower", "f", "flight"]))
# print(Solution().longestCommonPrefix(["f", "flow", "flight"]))
# print(Solution().longestCommonPrefix(["flower", "x", "flight"]))
# print(Solution().longestCommonPrefix(["baab","bacb","b","cbc"]))
# print(Solution().longestCommonPrefix(["flower", "flight", "x"]))
print(Solution().longestCommonPrefix(["dog", "racecar", "car"]))
