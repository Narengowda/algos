
x = [6,41,3,8,3,4,1,77,9,5,82, 1]

def merge(x):
    if len(x) == 1:
        return x

    left = merge(x[:int(len(x)/2)])
    right = merge(x[int(len(x)/2):])

    merged = []

    for i in range(len(left) + len(right)):
        if not left:
            merged += right
            break
        if not right:
            merged += left
            break

        if left[:1] > right[:1]:
            merged.extend(right[:1])
            right = right[1:]
        else:
            merged.extend(left[:1])
            left = left[1:]
    return merged

print(merge(x))
