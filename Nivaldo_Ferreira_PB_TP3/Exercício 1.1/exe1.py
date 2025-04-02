class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert_rec(self.root, key)

    def _insert_rec(self, node, key):
        if node is None:
            return Node(key)
        if key < node.key:
            node.left = self._insert_rec(node.left, key)
        else:
            node.right = self._insert_rec(node.right, key)
        return node

    def inorder(self):
        self._inorder_rec(self.root)

    def _inorder_rec(self, node):
        if node:
            self._inorder_rec(node.left)
            print(node.key, end=" ")
            self._inorder_rec(node.right)

    def preorder(self):
        self._preorder_rec(self.root)

    def _preorder_rec(self, node):
        if node:
            print(node.key, end=" ")
            self._preorder_rec(node.left)
            self._preorder_rec(node.right)

    def postorder(self):
        self._postorder_rec(self.root)

    def _postorder_rec(self, node):
        if node:
            self._postorder_rec(node.left)
            self._postorder_rec(node.right)
            print(node.key, end=" ")

bst = BST()
for value in [50, 30, 70, 20, 40, 60, 80]:
    bst.insert(value)

print("In-order:")
bst.inorder()
print("\nPre-order:")
bst.preorder()
print("\nPost-order:")
bst.postorder()