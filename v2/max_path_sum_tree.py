
tree = [10, 0, 25, -1, 21, 16, 32]

class Node(object):
    def __init__(self, value, left=None, right=None):
        self.left = left
        self.right = right
        self.value = value
        self.maxsum = 0


def children(i):
    return (i*2) + 1, (i*2) +2

# Generates tree from array
def gen_tree(i):
    if i >= len(tree):
        return None

    value = tree[i]
    l, r = children(i)
    return Node(value, gen_tree(l), gen_tree(r))



bst = gen_tree(0)
max_sum = 0

def maxsumgen(node):
    global max_sum

    if not node:
        return 0

    l = maxsumgen(node.left)
    r = maxsumgen(node.right)
    if (l + node.value + r) > max_sum:
        max_sum = l + node.value + r

    return l + node.value if l > r else r + node.value


maxsumgen(bst)
pass
