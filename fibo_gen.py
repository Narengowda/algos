


def fibgen(n):
    res = []
    for i in range(1, n+1):
        if i <= 2:
            out = i
        else:
            out = res[-1] + res[-2]
        res.append(out)
        yield out



print([x for x in fibgen(5)])
