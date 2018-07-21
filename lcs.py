
c = ['', 'a', 'b', 'c', 'd', 'c', 'b', 'a']
r = ['', 'd', 'c', 'b', 'a', 'a', 'b', 'c']
c = ['', 'x', 'x', 'x', 'x', 'x', 'x', 'x']
res = [
    [0,0,0,0,0,0,0, 0],
    [0,0,0,0,0,0,0, 0],
    [0,0,0,0,0,0,0, 0],
    [0,0,0,0,0,0,0, 0],
    [0,0,0,0,0,0,0, 0],
    [0,0,0,0,0,0,0, 0],
    [0,0,0,0,0,0,0, 0],
    [0,0,0,0,0,0,0, 0]
]
for ri in range(1, len(r)):
    for ci in range(1, len(c)):
        if c[ci] == r[ri]:
            print c[ci], ri, ci
            res[ri][ci] = res[ri-1][ci-1] + 1
        else:
            res[ri][ci] = max([res[ri-1][ci], res[ri][ci-1]])

print r
for i, r in enumerate(res):print c[i], r



