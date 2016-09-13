x = [4,2,7,9,3,2,6,8,5,3,2,22,2,4,677,8,9,6,54,32,45,346]


def bubble(data):
    dl = len(data)
    for i in range(dl-1):
        for j in range(dl-1):
            if data[j] > data[j+1]:
                data[j+1], data[j] = data[j], data[j+1]
    print data


bubble(x)
