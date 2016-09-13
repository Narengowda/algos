a = 'ABCDGH'
b = 'AEDFHR'

#http://www.geeksforgeeks.org/dynamic-programming-set-4-longest-common-subsequence/

def oslen(x, y):
    print x,y
    if not( x and y):
        return 0

    if x[-1] == y[-1]:
        return 1 + oslen(x[0: -1], y[0:-1])
    else:
        return max(oslen(x, y[0:-1]), oslen(x[0:-1], y))

print oslen(a, b)
