class Solution:
    def twoSum(self, nums: list, target: int) -> list:
        map = {}
        for i, j in enumerate(nums):
            diff = target - j
            if diff in map:
                return [map[diff], i]
            else:
                map[j] = i


# print(Solution().twoSum([2, 7, 11, 15], 9))
# print(Solution().twoSum([3, 2, 4], 6))
print(Solution().twoSum([3, 3], 6))
