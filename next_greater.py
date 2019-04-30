
strx = 'abcd'

def permutation(i, y):
    if len(y) == 1:
        return y

    out = []
    for i in range(len(y)):
        for p in permutation(i+1, y[0:i] + y[i+1:]):
            out.append(y[i] + p)

    return out

print(permutation('', strx))

