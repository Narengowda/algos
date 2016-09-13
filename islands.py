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
    out['l'] = (x-1, y) if (x-1) >= 0 else None
    out['lt'] = (x-1, y-1) if ((x-1) >= 0) and ((y-1) >= 0) else None
    out['ld'] = (x-1, y+1) if ((x-1) >= 0) and ((y+1) <= len_y-1) else None
    out['r'] = (x+1, y) if (x+1) <= len_x-1 else None
    out['rt'] = (x+1, y-1) if ((x+1) <= len_x-1) and (y-1 >=0) else None
    out['rd'] = (x+1, y +1) if ((x+1) <= len_x-1) and (y+1 <= len_y-1) else None
    out['t'] = (x, y-1) if (y-1) >= 0 else None
    out['d'] = (x, y+1) if (y+1) <= len_y-1 else None
    out['d'] = (x, y+1) if (y+1) <= len_y-1 else None
    return [_ for _ in out.values() if _ and i[_[0]][_[1]] == 1]

nodes = []

islands = []

for xx in range(len_x):
    for yy in range(len_y):
        n = i[xx][yy]
        if n == 1:
            nodes.append((xx, yy))

stack = deque()

for node in nodes:
    if node not in visited:
        stack.append(node)
        lands = []
        while len(stack):
            cnode = stack.pop()
            if cnode not in visited:
                lands.append(cnode)
                siblings = get_siblings(*cnode)
                siblings = [s for s in siblings if s not in visited]
                visited.append(cnode)
                stack.extend(siblings)
        islands.append(lands)

print 'Islands co-ordinates = ', islands
print 'Number of islands are = ', len(lands)





