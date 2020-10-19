"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if: Open brackets must be closed by the same type of brackets and Open brackets must be closed in the correct order.

Input: s = "()[]{}"
Output: true

Input: s = "([)]"
Output: false

https://leetcode.com/problems/valid-parentheses/discuss/9178/Short-java-solution
"""


class Solution:
    def isValid(self, s: str) -> bool:

        if len(s) < 2: return False

        mapping = {
            ')': '(',
            ']': '[',
            '}': '{'
        }


        stack = []

        for i in s:

            if i in mapping:
                if not stack: return False
                bracket = stack.pop()
                if bracket != mapping[i]:
                    return False
            else:
                stack.append(i)

        return not stack


# print(Solution().isValid('()[]{}'))
# print(Solution().isValid('(())'))
# print(Solution().isValid('{[()]}'))
# print(Solution().isValid(')'))
print(Solution().isValid('()'))
