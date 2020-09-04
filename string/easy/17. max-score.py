"""
Given a string s of zeros and ones, return the maximum score after splitting the string into two non-empty substrings (i.e. left substring and right substring)
The score after splitting a string is the number of zeros in the left substring plus the number of ones in the right substring.

https://leetcode.com/problems/maximum-score-after-splitting-a-string/discuss/597740/Java-StraightForward

Input: s = "011101"
Output: 5 Explanation: All possible ways of splitting s into two non-empty substrings are:
left = "0" and right = "11101", score = 1 + 4 = 5 left = "01" and right = "1101", score = 1 + 3 = 4 left = "011" and right = "101", score = 1 + 2 = 3
left = "0111" and right = "01", score = 1 + 1 = 2 left = "01110" and right = "1", score = 2 + 1 = 3

Input: s = "00111"
Output: 5
"""


class Solution:
    def maxScore(self, s: str) -> int:

        # no need of map
        if s[0] == '0':
            count_at_each_indx = {0: [1, 0]}
        else:
            count_at_each_indx = {0: [0, 0]}

        for i in range(1, len(s)):
            if s[i] == '0':
                count_at_each_indx[i] = [count_at_each_indx[i - 1][0] + 1, 0]
            else:
                count_at_each_indx[i] = [count_at_each_indx[i - 1][0], 0]

        if s[i] == '1':
            count_at_each_indx[i][1] = 1
        else:
            count_at_each_indx[i][1] = 0

        for i in range(len(s) - 2, -1, -1):
            if s[i] == '1':
                count_at_each_indx[i] = [count_at_each_indx[i][0], count_at_each_indx[i + 1][1] + 1]
            else:
                count_at_each_indx[i] = [count_at_each_indx[i][0], count_at_each_indx[i + 1][1]]

        total = 0

        #3 passes can be reduced to 2 passes by doing below comparison in the above loop

        for i in range(1, len(s)):
            total = max(total, count_at_each_indx[i - 1][0] + count_at_each_indx[i][1])

        return total


# print(Solution().maxScore('011101'))
# print(Solution().maxScore('01001'))
# print(Solution().maxScore('00111'))
# print(Solution().maxScore('1111'))
print(Solution().maxScore('0000'))
