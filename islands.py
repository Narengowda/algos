from collections import deque


i = [[1,1,0,0,0],
     [0,1,0,0,1],
     [1,0,0,1,1],
     [0,0,0,0,0],
     [1,0,1,0,1]]

len_y = len(i)
len_x = len(i[0])

visited = []

def get_siblings(x, y):
    out = {}

    # Dirty way of computing siblings/neighbors
    # Left siblings
    out['l'] = (x-1, y) if (x-1) >= 0 else None
    out['lt'] = (x-1, y-1) if ((x-1) >= 0) and ((y-1) >= 0) else None
    out['ld'] = (x-1, y+1) if ((x-1) >= 0) and ((y+1) <= len_y-1) else None

    # right siblings
    out['r'] = (x+1, y) if (x+1) <= len_x-1 else None
    out['rt'] = (x+1, y-1) if ((x+1) <= len_x-1) and (y-1 >=0) else None
    out['rd'] = (x+1, y +1) if ((x+1) <= len_x-1) and (y+1 <= len_y-1) else None

    # top siblings
    out['t'] = (x, y-1) if (y-1) >= 0 else None

    # down siblings
    out['d'] = (x, y+1) if (y+1) <= len_y-1 else None
    out['d'] = (x, y+1) if (y+1) <= len_y-1 else None

    # return only if cell is valid
    return [co_ords for co_ords in out.values() if co_ords and i[co_ords[0]][co_ords[1]] == 1]


stack = deque()
islands = []


def filter_nodes():
    return [(xx, yy) for xx in range(len_x) for yy in range(len_y) if i[xx][yy] == 1]

def BFS(nodes):
    for node in nodes:
        # If already visited then it will be part of connected cell
        # or invalid
        if node in visited:
            continue

        # put it in queue
        stack.append(node)
        lands = []

        while len(stack):
            cnode = stack.pop()

            if cnode in visited:
                continue

            lands.append(cnode)
            siblings = get_siblings(*cnode)
            siblings = [s for s in siblings if s not in visited]

            # update queue with siblings
            visited.append(cnode)
            stack.extend(siblings)

        islands.append(lands)


def main():
    nodes = filter_nodes()
    BFS(nodes)
    print 'Islands co-ordinates = ', islands
    print 'Number of islands are = ', len(islands)

main()



