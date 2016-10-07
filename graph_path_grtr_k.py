#  Given a graph a source verte in the graph and a number k, find if there is a
#  simple path(without cycle) starting from given source and ending at any other
#  vertex
#
#
graph = {
    0: {
        1: 4,
        7: 8
    },
    1: {
        2: 8,
        7: 11
    },
    2: {
        1: 8,
        8: 2,
        3: 7,
        5: 4,
    },
    3: {
        4: 9,
        5: 14,
        2: 7,
    },
    4: {
        3: 9,
        5: 10
    },
    5: {
        4: 10,
        2: 4,
        6: 2,
        3: 14
    },
    6: {
        8: 6,
        5: 2,
        7: 1
    },
    7: {
        6: 1,
        8: 7,
        0: 8
    },
    8: {
        2: 2,
        6: 6,
        7: 7
    }
}

upto = 58

def tracepath(node, total, visited):
    nodes = graph[node]
    paths = nodes.keys()

    for path in paths:
        if path not in visited:
            cost = nodes[path]
            total += cost
            if total >= upto:
                print "Found path: ", visited, ' Total cost: ',total
                return
            else:
                new = visited[:]
                new.append(path)
                tracepath(path, total, new)


tracepath(0, 0, [0])











