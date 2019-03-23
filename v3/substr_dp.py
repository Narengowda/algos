import pprint


x = "doggo"
y = "foggd"


data = [0 for i in range(len(x))]
data = [data[::] for i in range(len(y))]
pprint.pprint(data)

for i in range(len(data[0])):
    data[0][i] = i

for j in range(len(data)):
    data[j][0] = j


for i in range(1, len(x)):
    for j in range(1, len(y)):
        a = x[i - 1]
        b = y[j - 1]
        if a == b:
            data[i][j] = data[i - 1][j - 1] + 1
        else:
            data[i][j] = 0

pprint.pprint(data)
