"""
Given a string, find the first non-repeating character in it and return its index. If it doesn't exist, return -1.

faster: https://leetcode.com/problems/first-unique-character-in-a-string/discuss/86351/Python-3-lines-beats-100-(~-60ms)-!

s = "leetcode"
return 0.

s = "loveleetcode"
return 2.

"""


class Solution:
    def firstUniqChar(self, s: str) -> int:
        counter = {}
        for i in s:
            counter[i] = counter.get(i, 0) + 1

        for i in range(len(s)):
            if counter[s[i]] == 1:
                return i

        return -1


# print(Solution().firstUniqChar('leetcode'))
# print(Solution().firstUniqChar('loveleetcode'))
print(Solution().firstUniqChar('a'))
