"""
Write a function that reverses a string. The input string is given as an array of characters char[].

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

https://leetcode.com/problems/reverse-string/discuss/80946/Python2.7-(3-solutions:-Recursive-Classic-Pythonic)

Input: ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]

Input: ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
"""


class Solution:
    def reverseString(self, s: list) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # s = s[::-1]
        i = 0
        j = len(s) - 1
        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1

        return s


# print(Solution().reverseString(["h", "e", "l", "l", "o"]))
print(Solution().reverseString(["H", "a", "n", "n", "a", "h"]))
