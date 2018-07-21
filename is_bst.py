from collections import defaultdict


tree = [10, 0, 25, -1, 21, 16, 32]

class Node(object):
    def __init__(self, value, left=None, right=None):
        self.left = left
        self.right = right
        self.value = value


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

# Checks is BST
def is_bst(node, mini, maxi):
    if not(node):
        return True

    if not(node.value > mini and node.value < maxi):
        print("value = {} is not( > {} and {}) ".format(node.value, mini, maxi))
        return False
    return is_bst(node.left, mini, node.value) and is_bst(node.right, node.value, maxi)



# print(is_bst(bst, -9999999999, 9999999999))


# print left view
def left_view(node):
    if not node:
        return
    print(node.value)
    left_view(node.left)

# left_view(bst)



# Provides bottom view of the tree
scored_dict = {}
def bottom_view(node, score=0):
    if not node:
        return

    scored_dict[score] = node.value

    bottom_view(node.left, score-1)
    bottom_view(node.right, score+1)

# bottom_view(bst)
# print(scored_dict)

# Provides bottom view of the tree
virtical_dict = defaultdict(list)
def virtical_view(node, score=0):
    if not node:
        return

    virtical_dict[score].append(node.value)

    virtical_view(node.left, score-1)
    virtical_view(node.right, score+1)


# Prints virtical representation of tree
def gen_vertical_view(bst):
    virtical_view(bst)
    vd_list = sorted(virtical_dict.items())
    for i in vd_list:
        print(i[1])

# gen_vertical_view(bst)

# -------------------------------------

tree = [1, 2, 2, 3, 4, 4, 3, 4]
sym_bst = gen_tree(0)


def is_symmetric(node):
    left = iiiis_symmetric(node.left)
    right = iiiis_symmetric(node.right)
    print("left = {} right = {}".format(left, right))

    if left == right[::-1]:
        return True
    return False

def iiiis_symmetric(node):
    if not node:
        return []

    lv = iiiis_symmetric(node.left)
    rv = iiiis_symmetric(node.right)
    return lv + [node.value] + rv

print(is_symmetric(sym_bst))

max_ll = {}
def max_sum_leaf_to_leaf(node):



