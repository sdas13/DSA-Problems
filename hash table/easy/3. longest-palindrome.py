"""
Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.

https://leetcode.com/problems/longest-palindrome/discuss/89604/Simple-HashSet-solution-Java

Input: s = "abccccdd"
Output: 7
Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.
"""


class Solution:
    def longestPalindrome(self, s: str) -> int:
        counts = {}  # dict not required, set would just do

        max_len = 0
        for i in s:
            counts[i] = counts.get(i, 0) + 1
            if counts[i] == 2:
                max_len += 1
                del counts[i]

        if len(counts.keys()) > 0: return max_len + 1

        return max_len


print(Solution().longestPalindrome('abccccdd'))
