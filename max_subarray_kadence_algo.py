inp = [-2, -3, 4, -1, -2, 1, 5, -3]

a = []
s = []

for i in inp:

    if ((not a) and (i > 0)) or a:
        a.append(i)


    if (i > sum(s)):
        s = [i]

    if sum(s) < sum(a):
        s = a[::]

    print 's = ',s,'sum=',sum(s),  'a=',a,'  sum=',sum(a)

