x = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]


def minjump(i, hop):

    if i >= len(x):
        print("reached")
        return hop

    val = x[i]
    travs = []

    for j in range(1, val + 1):
        rethop = minjump(i + j, hop + 1)
        travs.append(rethop)

    return min(travs)


print(minjump(0, 0))
