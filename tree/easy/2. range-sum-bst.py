"""
Given the root node of a binary search tree, return the sum of values of all nodes with a value in the range [low, high].

       10
      / \
    5   15
  / \     \
 3  7     18

Input: root = [10,5,15,3,7,null,18], low = 7, high = 15
Output: 32

Input: root = [10,5,15,3,7,13,18,1,null,6], low = 6, high = 10
Output: 23
"""
from BST import BST, Node


class Solution:
    sum_range = 0

    def rangeSumBST(self, root: Node, L: int, R: int) -> int:
        self._inorder(root, L, R)
        return self.sum_range

    def _inorder(self, root, L, R):

        if root is None:
            return

        if L <= root.data <= R:
            self.sum_range += root.data

        if L < root.data:
            self._inorder(root.left, L, R)

        if root.data < R:
            self._inorder(root.right, L, R)


bst = BST()
bst.insert_node(10)
bst.insert_node(5)
bst.insert_node(3)
bst.insert_node(7)
bst.insert_node(15)
bst.insert_node(18)
bst.insert_node(1)
bst.insert_node(6)

# print(Solution().rangeSumBST(bst.root, 7, 15))
print(Solution().rangeSumBST(bst.root, 6, 10))
