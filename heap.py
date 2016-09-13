import math

x = [1, 23, 342, 1, 7, 23, 4, 11, 4, 12, 10]

def parent_index(child_index):
    # n/2 - 1
    return int(math.ceil(float(child_index)/2) - 1)


def children_index(parent_index):
    x = (2 * parent_index)
    return x+1, x+2

lenx = len(x)


def swap(data, maxheap=False):
    mod = False
    for i in range(lenx-1, 0, -1):
        parent = parent_index(i)

        if data[parent] < data[i] and maxheap:
            data[parent], data[i] = data[i], data[parent]
            mod = True

        if data[parent] > data[i] and not maxheap:
            data[parent], data[i] = data[i], data[parent]
            mod = True
    return mod



def max_heap(data):
    mod = True
    while mod:
        mod = swap(data, maxheap=True)
    print 'MAX heap : ', data

def min_heap(data):
    mod = True
    while mod:
        mod = swap(data)
    print 'MIN heap : ', data


max_heap(x[::])
min_heap(x[::])
