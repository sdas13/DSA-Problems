"""
Given an array arr of positive integers sorted in a strictly increasing order, and an integer k. Find the kth positive integer that is missing from this array.

Input: arr = [2,3,4,7,11], k = 5
Output: 9 The missing positive integers are [1,5,6,8,9,10,12,13,...]. The 5th missing positive integer is 9.

Input: arr = [1,2,3,4], k = 2
Output: 6 The missing positive integers are [5,6,7,...]. The 2nd missing positive integer is 6.
"""


class Solution:
    def findKthPositive(self, arr: list, k: int) -> int:

        i = 1
        while k != 0:
            if i == arr[0]:
                break
            else:
                i += 1
                k -= 1

        if k == 0: return i - 1

        if len(arr) == 1: return arr[0] + k

        for i in range(len(arr) - 1):
            diff = arr[i + 1] - arr[i]
            if diff > 1:
                if diff > k:
                    return arr[i] + k
                elif diff == k:
                    k = 1
                else:
                    k = k - diff + 1

        return arr[i + 1] + k


# print(Solution().findKthPositive([1, 2, 3, 4], 1))
# print(Solution().findKthPositive([1, 2, 3, 4], 5))
# print(Solution().findKthPositive([1, 2, 3, 4, 6], 1))
# print(Solution().findKthPositive([1, 2, 3, 4, 7], 3))
# print(Solution().findKthPositive([1, 2, 3, 4, 7, 8], 3))
# print(Solution().findKthPositive([1, 2, 3, 4, 7, 9], 3))
# print(Solution().findKthPositive([1, 2, 3, 4, 9], 10))
# print(Solution().findKthPositive([2, 3, 4, 7, 11], 5))
# print(Solution().findKthPositive([1, 2, 3, 4], 2))
print(Solution().findKthPositive([4, 5], 4))
