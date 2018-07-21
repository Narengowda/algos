tree = [1,2,3,4,5]

def children(i):
    l,r = (i*2) + 1, (i*2)+2
    if l >= len(tree):
        l = None
    if r >= len(tree):
        r = None
    return l, r

def parent(i):
    if i%2:
        return (i-1)/2
    else:
        return (i-2)/2

def in_order(ni):
    li , ri = children(ni)
    print("{}{}: li-{} ri-{}".format(' '*ni, ni, li, ri))

    ret = []
    ld = rd = None
    if li:
        ld = in_order(li)
    if ri:
        rd = in_order(ri)
    nd = tree[ni]

    ret.extend(ld or [])
    ret.extend([nd] or [])
    ret.extend(rd or [])
    print("{}{}: returning {}").format(' '*ni, ni, ret)
    return ret

def pre_order(ni):
    li , ri = children(ni)
    print("{}{}: li-{} ri-{}".format(' '*ni, ni, li, ri))

    ret = []
    ld = rd = None
    if li:
        ld = in_order(li)
    if ri:
        rd = in_order(ri)
    nd = tree[ni]

    ret.extend([nd] or [])
    ret.extend(ld or [])
    ret.extend(rd or [])
    print("{}{}: returning {}").format(' '*ni, ni, ret)
    return ret



# print(in_order(0))

print(pre_order(0))


