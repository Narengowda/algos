import random
from time import sleep

tree = [4,32,45, 3,2,7,3,8,54,38,88]



def parent(x):
    if x % 2:
        return (x - 1)/2
    rturn (x/2) - 1

def children(x):
    lc = (x*2) + 1
    rc = x * 2
    return lc if lc < len(tree) else None, rc if rc < len(tree) else None


def heapify(i):
    lc, rc = children(i)
    if lc:
        heapify(lc)
    if rc:
        heapify(rc)

    if lc and tree[lc] < tree[i]:
        tree[i], tree[lc] = tree[lc], tree[i]
    if rc and tree[rc] < tree[i]:
        tree[i], tree[rc] = tree[rc], tree[i]





