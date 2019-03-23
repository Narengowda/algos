import math

inp = "PAYPALISHIRING"


n = 4
mat = ["" for i in range(4)]

direc = "d"
c = 0
for i in inp:

    mat[c] += i

    if c == n - 1:
        direc = "u"

    if c == 0:
        direc = "d"

    if direc == "d":
        c += 1
    else:
        c -= 1

for m in mat:
    print(m)
