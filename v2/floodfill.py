img = [
[1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 0, 0],
[1, 0, 0, 1, 1, 0, 1, 1],
[1, 2, 2, 2, 2, 0, 1, 0],
[1, 1, 1, 2, 2, 0, 1, 0],
[1, 1, 1, 2, 2, 2, 2, 0],
[1, 1, 1, 1, 1, 2, 1, 1],
[1, 1, 1, 1, 1, 2, 2, 1],
]

point = (4, 4)
color = 3

lenx = 8
leny = 8

visited = []

def next(x, y):
    return [[x+1, y], [y+1, x], [x-1, y], [x, y-1]]


def flood_fill(x, y):
    if x < 0 or x >= lenx:
        return

    if y < 0 or y >= leny:
        return


    if img[x][y] == 2:
        img[x][y] = color

    visited.append([x,y])

    moves = next(x, y)
    for move in moves:
        if move not in visited:
            flood_fill(*move)


flood_fill(*point)
for i in img:print i

