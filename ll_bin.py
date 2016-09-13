
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


ll = genll(a)

# or get len by iterating over LL
len_a = len(a) - 1


def deci(l, count=0):

    base = l.value

    if l.link:
        value = deci(l.link, count+1)
        print 'inter ', (base ** (len_a - count)) + value, (len_a - count)
        return ((2 ** (len_a - count)) * base) + value
    else:
        print "end", base ** (len_a - count), base, (len_a - count)
        return (2 ** (len_a - count)) * base

print deci(ll)

