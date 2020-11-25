"""
Give a string s, count the number of non-empty (contiguous) substrings that have the same number of 0's and 1's,
and all the 0's and all the 1's in these substrings are grouped consecutively.

https://leetcode.com/problems/count-binary-substrings/solution/

Input: "00110011"
Output: 6
Explanation: There are 6 substrings that have equal number of consecutive 1's and 0's: "0011", "01", "1100", "10", "0011", and "01".

Input: "10101"
Output: 4
Explanation: There are 4 substrings: "10", "01", "10", "01" that have equal number of consecutive 1's and 0's.
"""


class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        count0 = 0
        count1 = 0
        res = 0
        prev = None
        for i in s:
            if i == '0':
                if prev == 1: count0 = 0
                prev = 0
                count0 += 1
                if count1 > 0:
                    res += 1
                    count1 -= 1

            if i == '1':
                if prev == 0: count1 = 0
                prev = 1
                count1 += 1
                if count0 > 0:
                    res += 1
                    count0 -= 1

        return res


# print(Solution().countBinarySubstrings('00110011'))
# print(Solution().countBinarySubstrings('10101'))
# print(Solution().countBinarySubstrings('000111'))
print(Solution().countBinarySubstrings('111101000'))
