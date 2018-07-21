mat = [ [1, 0, 1, 1, 1, 1, 0, 1, 1, 1 ],
        [1, 0, 1, 0, 1, 1, 1, 0, 1, 1 ],
        [1, 1, 1, 0, 1, 1, 0, 1, 0, 1 ],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 1 ],
        [1, 1, 1, 0, 1, 1, 1, 0, 1, 0 ],
        [1, 0, 1, 1, 1, 1, 0, 1, 0, 0 ],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1 ],
        [1, 0, 1, 1, 1, 1, 0, 1, 1, 1 ],
        [1, 1, 0, 0, 0, 0, 1, 0, 0, 1 ]];


visited = []
dest = [len(mat)-1, len(mat[0])-1]

print 'dest', dest
def next(x, y):
    return [[x+1, y], [x, y+1], [x-1, y], [x, y-1], [x+1, y+1], [x-1, y-1], [x-1, y+1], [x+1, y-1]]

def traverse(x, y, path):
    if [x, y] == dest:
        path.append([x,y])
        print path
        return

    for ne in next(x,y):
        if (ne not in visited) and (ne[0] <= dest[0]) and (ne[1] <= dest[1]) and (
            ne[0] >=0) and (ne[1] >= 0) and (mat[ne[0]][ne[1]] == 1):
            # print 'visiting {}'.format(ne)
            visited.append(ne)
            p = path[::]
            p.append([x,y])
            traverse(ne[0], ne[1], p)

traverse(0, 0, [])
