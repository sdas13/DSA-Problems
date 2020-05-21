"""
find out their common interest with the least list index sum

Input: list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 = ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]
Output: ["Shogun"]

Input: list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 = ["KFC","Shogun","Burger King"]
Output: ["Shogun"] index sum is "Shogun" with index sum 1 (0+1).

Input: list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 = ["KFC","Burger King","Tapioca Express","Shogun"]
Output: ["KFC","Burger King","Tapioca Express","Shogun"]

Input: list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 = ["KNN","KFC","Burger King","Tapioca Express","Shogun"]
Output: ["KFC","Burger King","Tapioca Express","Shogun"]
"""


class Solution:
    def findRestaurant(self, list1: list, list2: list) -> list:

        pass

    # print(Solution().findRestaurant(


#     ["Shogun", "Tapioca Express", "Burger King", "KFC"],
#     ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
# ))

print(Solution().findRestaurant(
    ["Shogun", "Tapioca Express", "Burger King", "KFC"],
    ["KFC", "Burger King", "Tapioca Express", "Shogun"]
))
