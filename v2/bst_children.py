import math

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
        return int((i-1)/2)
    return int(i/2) - 1


def tree_level():
    return math.ceil(math.log()) + 1


def bst():
    swap = False
    for ci in range(len(tree)-1, 0, -1):
        pi = parent(ci)
        print("\ncid={} parent index  = {}".format(ci, pi))
        cd = tree[ci]
        pd = tree[pi]
        print("Compare child: {}, parent: {}".format(cd, pd))

        # Right children
        if not(ci % 2):
            print("Right comp pd:{} > cd:{}".format(pd, cd))
            if pd > cd:
                print("swapping")
                tree[pi] = cd
                tree[ci] = pd
                swap = True
        else:
            if pd < cd:
                print("swapping")
                tree[pi] = cd
                tree[ci] = pd
                swap = True
    return swap


print("Before sort {}".format(tree_copy))


for i in range(100):
    print('-----------------')
    status = bst()
    print("Loop: {} status:{}".format(i, status))
    if not status:
        break

print("After sort {}".format(tree))
