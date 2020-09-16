"""
Given a string path, where path[i] = 'N', 'S', 'E' or 'W', each representing moving one unit north, south, east, or west, respectively. You start at the origin (0, 0) on a 2D plane and walk on the path specified by path.
Return True if the path crosses itself at any point, that is, if at any time you are on a location you've previously visited. Return False otherwise
https://leetcode.com/problems/path-crossing/discuss/709427/Detailed-Steps-using-Set-or-Java-Python

Input: path = "NES"
Output: false
Explanation: Notice that the path doesn't cross any point more than once.

Input: path = "NESWW"
Output: true
Explanation: Notice that the path visits the origin twice.
"""


class Solution:
    def isPathCrossing(self, path: str) -> bool:
        last_visited = (0, 0)
        points_visited = {last_visited}

        direction = {
            'N': 1,
            'S': -1,
            'E': 1,
            'W': -1
        }

        for i in path:

            if i in 'NS':
                y = direction[i] + last_visited[1]
                x = last_visited[0]
            else:
                x = direction[i] + last_visited[0]
                y = last_visited[1]

            if (x, y) in points_visited:
                return True

            last_visited = (x, y)
            points_visited.add((x, y))

        return False


# print(Solution().isPathCrossing('NES'))
# print(Solution().isPathCrossing('NESWW'))
print(Solution().isPathCrossing('ENENENWWSWSS'))
