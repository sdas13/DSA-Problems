"""
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.


In Pascal's triangle, each number is the sum of the two numbers directly above it.

Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]

"""


class Solution:
    def generate(self, numRows: int) -> list:
        if numRows == 0:
            return []

        res = [[1]]
        i = 1
        while i < numRows:
            temp_arr = [1]
            j = 1
            while j < i:
                temp_arr.append(res[i - 1][j - 1] + res[i - 1][j])
                j += 1
            temp_arr.append(1)
            res.append(temp_arr)
            i += 1

        return res


# print(Solution().generate(1))
# print(Solution().generate(2))
# print(Solution().generate(3))
print(Solution().generate(5))
