"""
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.

Input:

    3
   / \
  9  20
    /  \
   15   7

Depth: 3
"""


from BST import BST, Node


class Solution:
    def maxDepth(self, root: Node) -> int:
        if root is None:
            return 0

        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)

        return max(left_depth, right_depth) + 1  # +1 for the edge from the root connecting left and right subtree


bst = BST()
bst.insert_node(5)
bst.insert_node(1)
bst.insert_node(7)
bst.insert_node(6)
bst.insert_node(8)

print(Solution().maxDepth(bst.root))
