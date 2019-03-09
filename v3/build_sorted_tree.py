y = list(range(10))
import math
from collections import defaultdict

tree = defaultdict(list)


def build_tree(x, level):
    len_x = len(x)

    if len_x == 1:
        tree[level].append(x[0])
        return

    if len_x == 0:
        tree[level].append(None)
        return

    mid = int(math.ceil(len_x / 2))

    node = x[mid]

    tree[level].append(node)

    left = x[:mid]
    right = x[mid + 1 :]

    build_tree(left, level + 1)
    build_tree(right, level + 1)

build_tree(y, 0)
print(tree)
for i in tree:
    print tree[i],
