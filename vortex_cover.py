vortex = {
    'a': ['b'],
    'b': ['c', 'a'],
    'c': ['d', 'e'],
    'd': ['c', 'e', 'f', 'g'],
    'e': ['c', 'd', 'f'],
    'f': ['d', 'e'],
    'g': ['d'],
}

# Create graph with vertices eg: a: [ab], b: [ab, bc]
vortex = {k: [''.join(sorted([k, i])) for i in v] for k, v in vortex.items()}

# update number of vertices count in data to get order of keys to verify
data = {k: {'v': v, 'l': len(v)} for k,v in vortex.items()}
keys = sorted([(len(v), k) for k,v in vortex.items()], key= lambda x:x[0])

def check(k, check):
    k_keys = vortex.keys()
    k_keys.remove(k)

    for key in k_keys:
        if check in vortex[key]:
            return True
    return False


for k, v in keys:
    import pdb;pdb.set_trace()
    k_vals = vortex[v]

    # delete a node if all of its vertices are part of other node
    if all([check(v, val) for val in k_vals]):
        del(vortex[v])

print vortex









# data = {k: {'v': v, 'l': len(v)} for k,v in vortex.items()}
# keys = sorted([(len(v), k) for k,v in vortex.items()], key= lambda x:x[0], reverse=True)

# issued = []

# def get_allkeys(key):
    # try:
        # return [key]+vortex[key]
    # except:
        # return []

# for h, v in keys:
    # print h,v

    # if v not in vortex:
        # print 'NOOOOOOOOOOOOOOO'
        # continue

    # baseallkeys = get_allkeys(v)

    # loops = vortex.keys()
    # loops.remove(v)

    # for loop in loops:
        # allkeys = get_allkeys(loop)
        # print 'loop', loop, ' allkeys =',allkeys, 'base ',baseallkeys,set(baseallkeys) > set(allkeys)
        # if set(baseallkeys) > set(allkeys):
            # print 'REMOVINGGGGGGGGGGGG ',loop
            # del(vortex[loop])



# print  vortex

