x = [1, 2, 3, 4, 5, 6, 7, 8, None, None, None, None, None, None, 9, None]
valid_len = len(x)


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __repr__(self):
        return "[val:{} l:{} r:{}]".format(self.val, self.left, self.right)


def get_children(id):
    l, r = (id * 2) + 1, (id * 2) + 2

    if r < valid_len and l < valid_len:
        return l, r
    if r < valid_len:
        return r, None
    return None, None


def array_to_tree(pid):
    if pid is not None and pid < valid_len:
        l, r = get_children(pid)
        ln = array_to_tree(l)
        rn = array_to_tree(r)
        n = Node(x[pid])
        n.left = ln
        n.right = rn
        print(n)
        return n


tree = array_to_tree(0)


def t_width(n):
    if n:

