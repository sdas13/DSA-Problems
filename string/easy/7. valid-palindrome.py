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

        while i < j:
            if s[i] != s[j]:
                palindrome_from_left = s[i + 1:j + 1]
                palindrome_from_left_opposite = palindrome_from_left[::-1]
                is_palindrome_from_left = palindrome_from_left == palindrome_from_left_opposite
                palindrome_from_right = s[i:j]
                palindrome_from_right_opposite = palindrome_from_right[::-1]
                is_palindrome_from_right = palindrome_from_right == palindrome_from_right_opposite
                return is_palindrome_from_left or is_palindrome_from_right
            else:
                i += 1
                j -= 1

        return True


# print(Solution().validPalindrome('abcba'))
# print(Solution().validPalindrome('abcbxa'))
# print(Solution().validPalindrome('abcxba'))
# print(Solution().validPalindrome('racecar'))
# print(Solution().validPalindrome('radcecar'))
# print(Solution().validPalindrome('radcecabr'))
# print(Solution().validPalindrome('radcbecar'))
# print(Solution().validPalindrome('eccer'))
print(Solution().validPalindrome('lcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupucul'))
