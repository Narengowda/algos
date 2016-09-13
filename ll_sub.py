
from collections import namedtuple

class Node:

    def __init__(self, value, link=None, index=1):
        self.value = value
        self.link = link
        self.index = index

    def __str__(self):
        # space = ' '*((self.index+1) * 1)
        space = ' '
        return 'value: {}, link: [\n{}{}]'.format(self.value, space, self.link)

a = [1, 0, 0, 0]
b = [1]

len_a = len(a)
len_b = len(b)


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


a_ll = genll(a)
b_ll = genll(b)




if (int(''.join([str(aa) for aa in a])) > int(''.join([str(aa) for aa in b]))):



def subt(ll_a, ll_b):




