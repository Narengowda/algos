
from collections import namedtuple

#http://www.geeksforgeeks.org/decimal-equivalent-of-binary-linked-list/

a = [0,0,0,1, 1, 0, 0, 1, 0]

class Node:

    def __init__(self, value, link=None, index=1):
        self.value = value
        self.link = link
        self.index = index

    def __str__(self):
        space = ' '*((self.index+1) * 1)
        space = ' '
        return 'value: {}, link: [\n{}{}]'.format(self.value, space, self.link)


def genll(data):
    prev = None
    for i, v in enumerate(data):

        n = Node(value=v, index=i)
        if prev:
            prev.link = n
        else:
            start = n
        prev = n
    return start

def get_ll_length(ll):
    count = 0
    while ll:
        count += 1
        ll = ll.link
    return count


ll = genll(a)


def deci(ll):

    len_a = get_ll_length(ll) - 1
    out = 0
    count = 0
    while ll:
        temp = ((2 ** (len_a - count)) * ll.value)
        print temp, (len_a - count)
        out = out + temp
        ll = ll.link
        count += 1

    return out
print deci(ll)

