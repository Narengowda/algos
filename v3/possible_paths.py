# https://www.geeksforgeeks.org/count-possible-paths-top-left-bottom-right-nxm-matrix/
# Count all possible paths from top left to bottom right of a mXn matrix
# solve using recursion

nx, ny = 3,3

def paths(x, y, tp):

    if x> nx or y> ny:
        print(tp)
    else:
        tp.append((x,y))
        paths(x+1, y, tp[::])
        paths(x, y+1, tp[::])

paths(0, 0, [])
