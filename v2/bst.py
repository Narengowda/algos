
"""
             0
          /     \
        1         2
      /  \      /   \
    3     4    5     6


"""

tree = [1,3,4,6,7,8,10,13,14]
tree_copy = tree[::]
def children(i):
    l = (i * 2) + 1
    l = l if l < len(tree) else None
    r = (i * 2) + 2
    r = r if r < len(tree) else None
    return l, r

def parent(i):
    if (i % 2):
        return (i-1)/2
    return i/2



"""


"""

def bst(i):
    """Attempt to sort from parent"""
    """Fails to sort"""
    print("Current i = {}".format(i))
    li, ri = children(i)

    ld = tree[li] if li else None
    rd = tree[ri] if ri else None

    tmp = [tree[i], ld, rd]
    print("Tmp = {}".format(tmp))
    temp = sorted(filter(lambda x:x, tmp))
    print("sorted Tmp = {}".format(temp))

    if len(temp) == 3:
        tree[ri] = temp[2]
        tree[i ] = temp[1]
        tree[li] = temp[0]
    if len(temp) == 2:
        tree[i ] = temp[1]
        tree[li] = temp[0]
    if len(temp) == 1:
        tree[i] = temp[0]

    print("post swap bst {}".format(tree))
    if li:
        bst(li)
    if ri:
        bst(ri)

print("before bst {}".format(tree_copy))
for i in range(100):
    bst(0)
print("before bst {}".format(tree_copy))
print("after bst {}".format(tree))






















