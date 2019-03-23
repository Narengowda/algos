x = "doggo"
y = "foggd"


data = [0 for i in range(len(x) + 1)]
data = [data[::] for i in range(len(y) + 1)]
print(data)


for i in range(1, len(x)):
    for j in range(1, len(y)):
        a = x[i - 1]
        b = y[j - 1]
        if a == b:
            data[i][j] = data[i - 1][j - 1]
        else:
            data[i][j] = min(data[i - 1][j - 1], data[i][j - 1], data[i - 1][j]) + 1

print(data)
