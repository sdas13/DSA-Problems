"""
Write a function to find the longest common prefix string amongst an array of strings. If there is no common prefix, return an empty string ""

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
            temp = []
            while j < min(len(common_str), len(strs[i])):
                if common_str[j] == strs[i][j]:
                    temp.append(common_str[j])
                else:
                    break
                j += 1
            if not temp: return ""

            common_str = ''.join(temp)

        return common_str


# print(Solution().longestCommonPrefix(["flower", "flow", "flight"]))
# print(Solution().longestCommonPrefix(["flower", "f", "flight"]))
# print(Solution().longestCommonPrefix(["f", "flow", "flight"]))
# print(Solution().longestCommonPrefix(["flower", "x", "flight"]))
# print(Solution().longestCommonPrefix(["flower", "flight", "x"]))
print(Solution().longestCommonPrefix(["dog","racecar","car"]))
