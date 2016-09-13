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

a = [9,9,9,9]
b = [9,]

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



len_a = len(a)
len_b = len(b)

if len_a > len_b:
    pad = len_a - len_b
    b = [0] * pad + b

if len_b > len_a:
    pad = len_b - len_a
    a = [0] * pad + a


ll_a = genll(a)
print "a = ", ll_a


ll_b = genll(b)
print "b = ", ll_b


def sum_ll(a, b):

    tprev = None
    start = None

    while True:
        # import pdb; pdb.set_trace()  # XXX BREAKPOINT
        av = a.value
        bv = b.value

        tv = av + bv

        tn = Node(value=tv)

        if not tprev:
            tprev = tn
            start = tn
        else:
            tn.value = tv
            tprev.link = tn
            tprev = tn

        if a.link and b.link:
            a = a.link
            b = b.link
        else:
            return start


sll = sum_ll(ll_a, ll_b)

print sll

def rev_ll(ll):
    a = ll
    b = a.link
    a.link = None

    while True:
        c = b.link
        b.link = a

        if not c:
            return b

        a = b
        b = c




print sll
revll = rev_ll(sll)
print '---------------'
print revll

def spread(ll):
    sample = ll
    while True:
        # import pdb; pdb.set_trace()  # XXX BREAKPOINT


        if ll and ll.value > 9:
            link = ll.link

            val = ll.value
            ll.value = val % 10
            ll.link = Node(link=link, value=1)
            ll = link
        else:
            ll = ll.link

        if not ll:
            return sample



print rev_ll(spread(revll))



