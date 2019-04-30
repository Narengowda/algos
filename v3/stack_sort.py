stack = [42, 5, 2, 1, 8]


def rec(s):
    if len(s) == 1:
        return s

    x = s.pop()
    r = rec(s)

    return rev(x, r)


def rev(ele, s):
    if len(s) == 0:
        s.append(ele)
        return s

    x = s.pop()

    r = rev(ele, s)

    r.append(x)
    return r


print(rec(stack))
