"""
There is a matrix M*N. The matrix elements are either black or white. We call neighboring elements of the same color areas. You can pick any area and flip its color (i.e. change the color of all its elements). Given such a matrix find the minimal number of flips needed to make the whole matrix either black or white.

"""

import pprint

pp = pprint.PrettyPrinter(indent=4)

x = """\
B w B w B w B w B
w Y w w B w w w w
B w B B B B B w B
w w B B B B B w w
B B B B B B B B B
w w B B B B B w w
B w B B B B Y Y B
w Y w w B w w w w
B w B w B w B w B"""

x = x.split("\n")
data = [i.split(" ") for i in x]
pp.pprint(data)

# Try to find the connected components and flip the biggest component?

connected_components = []
visited = []
LX = len(data)
LY = len(data[0])


def get_siblings(x, y):
    out = {}
    out["l"] = (x - 1, y) if (x - 1) >= 0 else None
    out["lt"] = (x - 1, y - 1) if ((x - 1) >= 0) and ((y - 1) >= 0) else None
    out["ld"] = (x - 1, y + 1) if ((x - 1) >= 0) and ((y + 1) <= LY - 1) else None
    out["r"] = (x + 1, y) if (x + 1) <= LX - 1 else None
    out["rt"] = (x + 1, y - 1) if ((x + 1) <= LX - 1) and (y - 1 >= 0) else None
    out["rd"] = (x + 1, y + 1) if ((x + 1) <= LX - 1) and (y + 1 <= LY - 1) else None
    out["t"] = (x, y - 1) if (y - 1) >= 0 else None
    out["d"] = (x, y + 1) if (y + 1) <= LY - 1 else None
    out["d"] = (x, y + 1) if (y + 1) <= LY - 1 else None
    return [_ for _ in out.values() if _]


def is_in_component(point):
    for c in connected_components:
        if point in c:
            return True
    return False


def get_connected_components(x, y, value, component, visited):
    if not is_in_component((x, y)):
        component.append((x, y))

    sibs = get_siblings(x, y)
    for sib in sibs:
        if (
            data[sib[0]][sib[1]] == value
            and not is_in_component(sib)
            and (sib not in visited)
        ):
            visited.append(sib)
            component.append(sib)
            get_connected_components(sib[0], sib[1], value, component, visited)

    return component


def gen_cc():
    for i in range(LX):
        for j in range(LY):
            comp = get_connected_components(i, j, data[i][j], [], [])
            if comp:
                connected_components.append(comp + [data[i][j]])


def flip(cc, flip_color):
    for c in cc:
        data[c[0]][c[1]] = flip_color


def exec_flip():
    for i in range(1, 100):
        global connected_components
        connected_components = []
        gen_cc()
        sorted_components = sorted(connected_components, key=lambda x: len(x))

        if len(sorted_components) == 1:
            print("looks like we have flipped the colors. and took {} loops".format(i))
            exit()

        big_component = sorted_components[-1]
        second_big_component = sorted_components[-2]

        flip(big_component[:-1], second_big_component[-1])
        pp.pprint(data)


exec_flip()
# comp = get_connected_components(0, 8, data[0][8], [], [])
# pp.pprint(connected_components)
