import math
from collections import namedtuple
# http://www.geeksforgeeks.org/convert-a-binary-tree-to-a-circular-doubly-link-list/


x = [10, 12, 15, 25, 30, 36]
cll = []

node = namedtuple('node', 'left', 'right', 'value')


def get_level(num):
    return math.ceil(math.log(num, 2))


def get_parent(child):
    if child % 2:
        return child/2
    else:
        return (child+1)/2

def get_children(parent):
    l, r = abs((parent * 2) + 1), abs(parent *2) + 2

    if l >= len(x):
        return None, None
    else:
        return l, r


result = []
size = len(x)
level = get_level(len(x))
first = None
last = None


def track_parent(i, result):
    l, r = get_children(i)


    if l and not (l >= size):
        track_parent(l, result)

    result.append(x[i])

    if r and not (r >= size):
        track_parent(r, result)

    return result


print track_parent(0, result)
