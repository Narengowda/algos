x = [
[0,0,1,0,0,1],
[0,1,0,0,0,1],
[1,0,1,0,0,0],
[1,0,1,1,1,0],
[1,0,0,0,0,1],
[0,0,0,1,1,0]
]

n = len(x[0])

graph_list = [ ]


def route(i, j):
    new_i = i+1 if i+1 < n else None
    new_j = j+1 if j+1 < n else None

    r = d = c = None

    if new_j:
        r = (i, new_j)
    if new_i:
        d = (new_i, j)

    if new_i and new_j:
        c = (new_i, new_j)

    return r, c, d

out = {}

def graph(i, j, link):
    r, c, d = route(i, j)
    print(r,c,d)
    # import pdb; pdb.set_trace()  # XXX BREAKPOINT

    if x[i][j]:
        link.append((i,j))
    else:
        if link and len(set(link)) > 1:
            out[tuple(link)] = ''
        link = []

    if r:
        graph(r[0], r[1], link)

    if d:
        graph(d[0], d[1], link)

    if c:
        graph(c[0], c[1], link)



graph(0, 0, graph_list)


for o in out:
    print(o)




