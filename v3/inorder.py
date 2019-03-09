INORDER = "IN"
PREORDER = "PRE"
POSTORDER = "POST"


class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

    def __str__(self):
        return str(self.val)

    __repr__ = __str__


def traversal(node, typ):
    l = []
    r = []

    if node and node.left:
        l = traversal(node.left, typ)
    if node and node.right:
        r = traversal(node.right, typ)

    if typ == INORDER:
        return l + [node.val] + r
    if typ == PREORDER:
        return [node.val] + l + r
    return l + r + [node.val]


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print(traversal(root, typ=INORDER))
print(traversal(root, typ=POSTORDER))
print(traversal(root, typ=PREORDER))
