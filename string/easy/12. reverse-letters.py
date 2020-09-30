"""
Given a string S, return the "reversed" string where all characters that are not a letter stay in the same place, and all letters reverse their positions.

https://leetcode.com/problems/reverse-only-letters/solution/

Input: "a-bC-dEf-ghIj"
Output: "j-Ih-gfE-dCba"

Input: "Test1ng-Leet=code-Q!"
Output: "Qedo1ct-eeLg=ntse-T!"
"""


class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        i = 0
        j = len(S) - 1

        S = list(S)

        while i < j:
            if not S[i].isalpha():
                i += 1
            elif not S[j].isalpha():
                j -= 1
            else:
                S[i], S[j] = S[j], S[i]
                i += 1
                j -= 1

        return ''.join(S)


# print(Solution().reverseOnlyLetters('ab-cd'))
# print(Solution().reverseOnlyLetters('a-bC-dEf-ghIj'))
print(Solution().reverseOnlyLetters('Test1ng-Leet=code-Q!'))
