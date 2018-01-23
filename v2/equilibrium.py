x = [55, 5, 1, 10, 10, 10, 10, 10, 10, 1]

a = []
b = []

pi = 0
for i in x:
    pi = pi+i
    a.append(pi)


pi = 0
for i in x[::-1]:
    pi = pi+i
    b.append(pi)

print a,b
