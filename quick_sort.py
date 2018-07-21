data = [7, 2, 1, 6, 8,5, 3, 4]


def quick_sort(x):
    if not x: return []
    if len(x) == 1:
        return x
    if len(x) == 2:
        if x[0] > x[1]:
            return [x[1], x[0]]
        return x

    pivot = x[-1]
    l = []
    r = []
    for i in x:
        if i < pivot:
            l.append(i)
        elif i > pivot:
            r.append(i)

    print pivot,l,r
    lr = quick_sort(l)
    rr = quick_sort(r)
    return lr + [pivot] + rr

print quick_sort(data)

