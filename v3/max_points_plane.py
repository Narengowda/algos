#https://leetcode.com/problems/max-points-on-a-line/

import collections

x = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
x = [[1,1],[2,2],[3,3]]

combs = collections.defaultdict(int)


def slope(a, b):
    return ((b[1] - a[1]), (b[0] - a[0]))


for i in x:
    for j in x:
        if i != j:
            s = slope(i, j)
            combs[s] += 1

print(combs)

print(max(combs.values())+1)
