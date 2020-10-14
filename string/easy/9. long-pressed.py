"""
Your friend is typing his name into a keyboard. Sometimes, when typing a character c, the key might get long pressed, and the character will be typed 1 or more times.
You examine the typed characters of the keyboard. Return True if it is possible that it was your friends name, with some characters (possibly none) being long pressed.

https://leetcode.com/problems/long-pressed-name/discuss/183994/C%2B%2BJavaPython-Two-Pointers

Input: name = "alex", typed = "aaleex" Output: true Explanation: 'a' and 'e' in 'alex' were long pressed.

Input: name = "saeed", typed = "ssaaedd" Output: false Explanation: 'e' must have been pressed twice, but it wasn't in the typed output.

Input: name = "laiden", typed = "laiden" Output: true
"""


class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:

        i = 0
        j = 0
        while i < len(name):

            temp = name[i]

            if j == len(typed) or typed[j] != temp:
                return False

            typed_count = 0
            while j < len(typed) and typed[j] == temp:
                typed_count += 1
                j += 1

            name_count = 0
            while i < len(name) and name[i] == temp:
                name_count += 1
                i += 1

            if typed_count < name_count: return False

        if j < len(typed): return False

        return True


print(Solution().isLongPressedName('alex', 'aaleex'))
# print(Solution().isLongPressedName('aleex', 'aleeex'))
# print(Solution().isLongPressedName('saeed', 'saed'))
# print(Solution().isLongPressedName('saeed', 'ssaaedd'))
# print(Solution().isLongPressedName('leelee', 'lleeelee'))
# print(Solution().isLongPressedName('laiden', 'laiden'))
# print(Solution().isLongPressedName('alex', 'aaleexa'))
# print(Solution().isLongPressedName('alex', 'aaleex'))
