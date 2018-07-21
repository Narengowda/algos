#http://www.geeksforgeeks.org/in-place-convert-a-given-binary-tree-to-doubly-linked-list/

import math
from collections import namedtuple

class node(object):

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class llnode(object):

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        l_v = self.left.value if self.left else None
        r_v = self.right.value if self.right else None
        return "{}={}={}".format(l_v, self.value, r_v)


    def attach(self, val, side):
        valid_node = self
        while True:
            l = getattr(valid_node, side)
            if not l:
                break
            valid_node = l
        setattr(valid_node, side, val)


    __repr__ = __str__


data = [10, 12, 15, 25, 30, 36]


def is_left(i):
    return i % 2

def parent(i):
    # check if left
    if is_left(i):
        return (i-1) / 2
    else:
        return (i/2) - 1

def children(i):
    left = ((2 * i) + 1)

    if left >= len(data):
        left = None

    right = ((2 * i) + 2)
    if right >= len(data):
        right = None

    return left, right



def level(i):
    if not i:
        return 0
    else:
        return math.floor(math.log(i, 2)) + 1


def tree(i):
    print("creating node for {} but lenis {}".format(i, len(data)))
    n = node(value=data[i])

    l, r = children(i)
    print("l ={}   r={}".format(l, r))

    if l:
        n.left = tree(l)
    if r:
        n.right = tree(r)

    return n

# This creates tree
nd = tree(0)

def ll(i):
    cnd = llnode(data[i])
    lnd = rnd = None
    l, r = children(i)

    print("l ={}   r={}".format(l, r))

    if not (l and r):
        return cnd

    if l:
        lnd = ll(l)
    if r:
        rnd = ll(r)

    print("Got cnd:{} lnd:{} rnd:{}".format(cnd, lnd,rnd))

    if lnd:
        lnd.attach(cnd, 'right')
        cnd.left = lnd
    if rnd:
        rnd.attach(cnd, 'left')
        cnd.right = rnd

    ret = lnd  or cnd  or rnd
    print("returning {}".format(ret))
    return ret



double_ll = ll(0)
pass

