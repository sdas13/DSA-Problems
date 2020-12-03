"""
Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.

Input: "aba"
Output: True

Input: "abca"
Output: True
Explanation: You could delete the character 'c'.

"""


class Solution:
    def validPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1

        while i<j:
            if s[i]!=s[j]:
                s[i+1:j+1]

            else:
                i+=1
                j-=1

        return True

# print(Solution().validPalindrome('abcba'))
# print(Solution().validPalindrome('abcbxa'))
# print(Solution().validPalindrome('abcxba'))
# print(Solution().validPalindrome('racecar'))
# print(Solution().validPalindrome('radcecar'))
# print(Solution().validPalindrome('radcecabr'))
# print(Solution().validPalindrome('radcbecar'))
# print(Solution().validPalindrome('lcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupucul'))
