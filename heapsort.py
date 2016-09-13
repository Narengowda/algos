import math

inp = [1, 23, 342, 1, 7, 23, 4, 11, 4, 12, 10]

def parenti(child_index):
    # n/2 - 1
    return int(math.ceil(float(child_index)/2) - 1)


def swap(data, lenx, maxheap=False):
    mod = False
    for i in range(lenx-1, 0, -1):
        parent = parenti(i)

        if data[parent] < data[i] and maxheap:
            data[parent], data[i] = data[i], data[parent]
            mod = True

        if data[parent] > data[i] and not maxheap:
            data[parent], data[i] = data[i], data[parent]
            mod = True
    return mod


def max_heap(data):
    lenx = len(data)
    mod = True
    while mod:
        mod = swap(data, lenx, maxheap=True)
    return data


def heapsort(x):
    lenx = len(x)
    sorted_data = []
    for i in range(lenx):
        x = max_heap(x)
        sorted_data.append(x[0])
        del x[0]
    print sorted_data

heapsort(inp)
