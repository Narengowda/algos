import math

inp = [1,3,5,3,45,5,4,3,4,5345,34,54,2,3,456,2,3,2,5,55,444]

print 'input: ',inp

def bubble(data):
    dl = len(data)
    for i in range(dl-1):
        for j in range(dl-1):
            if data[j] > data[j+1]:
                data[j+1], data[j] = data[j], data[j+1]
    print data


# bubble(inp)
# Notes:
#
#----------------------------------------------------------

def selection(data):
    dl = len(data)

    for i in range(dl):
        min = data[i]
        min_ind = i
        for j in range(i, dl):
            if data[j] < min:
                min = data[j]
                min_ind = j

        print min, min_ind
        print '-'*8
        data[i], data[min_ind] = min, data[i]
    print 'sorted:', data

# selection(inp)
# Notes:
# Dont forget range(i, dl)
#----------------------------------------------------------

def insertion(data):
    dt = len(data)

    for i in range(dt):
        cur = data[i]
        for j in range(i, -1, -1):
            if data[j] < cur:
                del data[i]
                data.insert(j+1, cur)
                break

    print data

# insertion(inp)
# Note:
#----------------------------------------------------------


def parent_index(child_index):
    # n/2 - 1
    return int(math.ceil(float(child_index)/2) - 1)


def swap(data, lenx, maxheap=False):
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

# heapsort(inp)
# Note:
#----------------------------------------------------------



def splitter(x):

    lenx = len(x)

    if lenx == 2:
        if x[0] > x[1]:
            left, right = [x[1]], [x[0]]
        left, right = [x[0]], [x[1]]
    elif lenx in [0, 1]:
        return x
    else:
        left = x[:lenx/2]
        right = x[lenx/2:]


    lsorted = splitter(left)
    rsorted = splitter(right)
    merged_data = merger(lsorted, rsorted)
    return merged_data


def merger(l, r):
    j = 0
    for i in range(len(l)):
        for j in range(j, len(r)):
            if l[i] <= r[j]:
                r.insert(j, l[i])
                break
        else:
            r.insert(len(r), l[i])

    return r


def merge_sort(inp):
    print 'Merge sort: ',splitter(inp)


# merge_sort(inp)
# Note: dont forget lenx in [0 ,1] condition
#----------------------------------------------------------



















