"""
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Input: [7,1,5,3,6,4]
Output: 5

Input: [7,6,4,3,1]
Output: 0

"""


class Solution:
    def maxProfit(self, prices: list) -> int:
        min_point = float('inf')
        max_point = float('-inf')
        max_profit = 0

        for i in prices:
            if i <= min_point:
                min_point = i
                max_point = float('-inf')
                continue

            if i >= max_point:
                max_point = i
                diff = max_point - min_point
                if diff > max_profit:
                    max_profit = diff

        return max_profit



# print(Solution().maxProfit([7, 1, 5, 3, 6, 4]))
# print(Solution().maxProfit([7, 6, 4, 3, 1]))
print(Solution().maxProfit([10, 8, 12, 6, 21, 3, 7, 21, 18]))
