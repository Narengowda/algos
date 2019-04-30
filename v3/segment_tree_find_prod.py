x = [6, 2, 8, 1, 6, 2, 5]
k = 4

print(x)


def parent(i):
    return i / 2


def children(i):
    return i * 2, (i * 2) + 1


def build(l, r):
    print(">>>>> ", l, r, x[l:r])

    if sum(x[l:r]) % k == 0:
        print("divisable range", l, r)

    if (r - l) == 1 or r == l:
        return

    mid = (l + r) // 2

    build(l, mid)
    build(mid, r)


build(0, len(x))
