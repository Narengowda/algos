x = "GkGEGG"


def lpc(l, r):

    sub_str = x[l:r]
    print(sub_str)

    if len(sub_str) == 1:
        return 1

    if len(sub_str) == 2 and sub_str[0] == sub_str[-1]:
        return 2

    if sub_str[0] == sub_str[-1]:
        return lpc(l + 1, r - 1) + 2

    return max(lpc(l + 1, r), lpc(1, r - 1))


print(lpc(0, len(x)))
