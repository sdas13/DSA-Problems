class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:

    def __init__(self):
        self.root = None

    def insert_node(self, data):
        self.root = self._insert(self.root, data)

    def _insert(self, root, data):
        if root is None:
            node = Node(data)
            root = node
        elif data <= root.data:
            root.left = self._insert(root.left, data)
        else:
            root.right = self._insert(root.right, data)

        return root

    def search(self, data):
        return self._search(self.root, data)

    def _search(self, root, data):
        if root is None:
            return False
        if root.data == data:
            return True
        elif data <= root.data:
            return self._search(root.left, data)
        else:
            return self._search(root.right, data)

        return False

    def find_min(self):
        return self._min(self.root).data

    def _min(self, root):

        if root is None:
            return -1

        if root.left is None:
            return root

        return self._min(root.left)

    def find_max(self):
        return self._max(self.root).data

    def _max(self, root):

        if root is None:
            return -1

        if root.right is None:
            return root

        return self._max(root.right)

    def find_height(self):
        return self._height(self.root)

    def _height(self, root):

        if root is None:
            return -1

        left_subtree_height = self._height(root.left)
        right_subtree_height = self._height(root.right)

        return max(left_subtree_height, right_subtree_height) + 1

    # level order traversal
    def BFS(self):

        if self.root is None:
            return

        lst = [self.root]

        while lst:
            front = lst[0]
            print(front.data)
            lst.append(front.left) if front.left else None
            lst.append(front.right) if front.right else None

            lst.pop(0)

    def DFS(self):
        # self._pre_order(self.root)
        self._in_order(self.root)
        # self._post_order(self.root)

    def _pre_order(self, root):

        if root is None:
            return

        print(root.data)
        self._pre_order(root.left)
        self._pre_order(root.right)

    def _in_order(self, root):

        if root is None:
            return

        self._in_order(root.left)
        print(root.data)
        self._in_order(root.right)

    def _post_order(self, root):

        if root is None:
            return

        self._post_order(root.left)
        self._post_order(root.right)
        print(root.data)

    def check_BST(self):
        val = self._check_BST(self.root, float('-inf'), float('inf'))
        print(val)

    def _check_BST(self, root, lower, upper):

        if root is None:
            return True

        if lower <= root.data and root.data < upper:
            is_left_valid = self._check_BST(root.left, lower, root.data)
            is_right_valid = self._check_BST(root.right, root.data, upper)

            return is_left_valid and is_right_valid
        else:
            return False

    def delete_node(self, value):
        self._delete(self.root, value)

    def _delete(self, root, value):

        if root is None:
            return None

        if value < root.data:
            root.left = self._delete(root.left,
                                     value)
        # reducing the problem to left subtree, root of the subtree may change after deletion,
        # so returning the new root and attaching to parent, that's how the link in parent is being corrected

        elif value > root.data:
            root.right = self._delete(root.right, value)

        else:
            if root.left is None and root.right is None:
                del root
                root = None


            elif root.left is None:
                temp = root
                root = root.right
                del temp

            elif root.right is None:
                temp = root
                root = root.left
                del temp


            else:
                min_node = self._min(root.right)
                root.data = min_node.data
                root.right = self._delete(root.right, min_node.data)
        return root


bst = BST()
bst.insert_node(5)
bst.insert_node(3)
bst.insert_node(1)
bst.insert_node(2)
bst.insert_node(12)
bst.insert_node(10)
bst.insert_node(15)
bst.insert_node(11)
bst.insert_node(13)
bst.insert_node(14)
# bst.search(12)
# bst.search(15)
# bst.search(1)
# bst.find_min()
# bst.find_max()
# bst.find_height()
# bst.BFS()
# bst.DFS()
# bst.check_BST()
bst.delete_node(12)
