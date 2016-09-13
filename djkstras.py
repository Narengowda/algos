from pprint import pprint

x = {
    'o': {'a': 2, 'b': 5, 'c': 4,},
    'a': {'b':2, 'd': 7, 'f': 12, 'o': 2},
    'b': {'c': 1, 'e':3, 'd': 4, 'o': 5, 'a':2},
    'c': {'o':4, 'b': 1, 'e': 4},
    'd': {'a':7, 'b':4, 'e':1, 't':5},
    'e': {'c':4, 'b':3, 'd':1, 't':7},
    'f': {'a': 12, 't': 3},
    't': {'f':3, 'd':5, 'e':7}
}
print "given path"
pprint(x)


start, end = 'o', 't'
nodes_length = len(x.keys())
path_matrix = {l: 9999 for l in x.keys()}
path_matrix[start] = 0
visited_nodes = []

# PRINT
pprint(path_matrix)

history = []

def update_node_weight(node):
    if node in visited_nodes:
        return

    visited_nodes.append(node)
    node_value = path_matrix[node]

    next_nodes_to_visit = []
    branches = x[node]

    for branch_node, value in branches.items():
        previous_value = path_matrix[branch_node]
        print "--> node -> ",node, ' ---bn -> ', branch_node
        print 'curr value: ', node_value + value, ' prev val = ',previous_value
        new_val = node_value + value

        if new_val < previous_value:
            print "UPDATE"
            path_matrix[branch_node] = new_val

        next_nodes_to_visit.append(branch_node)

    history.append((node, path_matrix.copy().items()))
    print '----'* 10
    pprint (path_matrix)
    print '----'* 10

    [update_node_weight(future_node) for future_node in next_nodes_to_visit]


update_node_weight(start)
pprint(path_matrix)
pprint(history)


