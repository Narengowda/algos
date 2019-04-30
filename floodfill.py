

img = [
[1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 2, 0],
[1, 0, 0, 1, 0, 2, 1, 1],
[1, 2, 2, 2, 2, 0, 1, 0],
[1, 1, 1, 2, 2, 0, 1, 0],
[1, 1, 1, 2, 2, 2, 2, 0],
[1, 1, 1, 1, 1, 2, 1, 1],
[2, 2, 1, 1, 1, 2, 2, 1],
]


lenr = len(img)
lenc = len(img[0])

visited = []

def neighbours(r, c):
    return [[r+1, c], [r+1, c], [r-1, c], [r, c-1],
            [r+1, c+1], [r+1, c-1], [r-1, c-1], [r-1, c+1]]


def flood_fill(r, c, color, replace_color):
    if r < 0 or r >= lenr:
        return

    if c < 0 or c >= lenc:
        return

    if img[r][c] != color:
        return

    img[r][c] = replace_color

    visited.append([r, c])

    moves = neighbours(r, c)

    for move in moves:
        if move not in visited:
            flood_fill(move[0], move[1], color, replace_color)


def flood_img():
    print("Input")

    for i in img:print i
    replace_point = (4, 4)
    flood_fill(*replace_point, color=2, replace_color=3)

    print "-" * 25
    print "output"
    for i in img:print i


flood_img()
