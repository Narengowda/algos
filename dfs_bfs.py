tree = [0, 1, 2, 3, 4, 5, 6]

"""
             0
          /     \
        1         2
      /  \      /   \
    3     4    5     6


"""

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


output = []


# DFS using recursion
def traverse(i):
    cnd = tree[i]
    result = [cnd]
    li, ri = children(i)


    if li:
        ld = traverse(li)
        result.extend(ld)
    if ri:
        rd = traverse(ri)
        result.extend(rd)
    return result

print("DFS = {}".format(traverse(0)))


def queue(li, ri, queue):
    if li:queue = [li] + queue
    if ri:queue = [ri] + queue
    return queue

def stack(li, ri, stack):
    if ri:stack.append(ri)
    if li:stack.append(li)
    return stack

# One function for DFS and BFS
def dynamic_travers(trav):
    result = []
    queue = [0]
    while len(queue) > 0:
        now = queue.pop()
        result.append(tree[now])
        li, ri = children(now)
        queue = trav(li, ri, queue)
    return result

print("BFS = {}".format(dynamic_travers(trav=queue)))
print("DFS = {}".format(dynamic_travers(trav=stack)))

