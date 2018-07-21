x = [15,  -2,  2,  -8,  1,  7,  10, 23]

hash = {
}

for i in range(len(x)):
    s = sum(x[:i+1])
    if s == 0:
        print i

    print x[i] ,' hash = ',hash, '   i=',i, '  check sum ',s, ' in hash=',  s in hash
    hash[s] = i

