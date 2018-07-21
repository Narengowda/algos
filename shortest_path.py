data = [ # xxxxxxxxxxx
    [1, 1, 1, 1, 1],# y
    [1, 1, 1, 1, 1],# y
    [1, 0, 1, 1, 1],# y
    [1, 1, 1, 0, 1],# y
    [0, 0, 1, 1, 1],# y
]

mx = my = len(data[0])

destx = 4
desty = 4

def next(x, y):
    return x+1, y, x, y+1
            # right   # down

def find(x, y, sofar):
    # print '----->at {},{}'.format(x,y)

    if data[x][y] == 0:
        # print "Exit as its 0"
        return

    sofar.append((x,y))

    if x == destx and y == desty:
        print "yeyy", sofar


    rx, ry, dx, dy = next(x, y)
    # print "computed = right={}  down={}".format((rx, ry), (dx, dy))


    if rx < mx and ry < my:
        find(rx, ry, sofar[::])

    if dx < mx and dy < my:
        find(dx, dy, sofar[::])



print find(0, 0, [])


    # print 'at {},{}'.format(x,y)
    # rx, ry, dx, dy = next(x, y)
    # print rx, ry, dx, dy
    # sofar.append((x,y))

    # if data[x][y] != 0:

        # if rx < mx and ry < my:
            # find(rx, ry, sofar[::])
        # if dx < mx and dy < my:
            # print "Down"
            # find(dx, dy, sofar[::])

        # if x == destx and y == desty:
            # print "yeyy", sofar

