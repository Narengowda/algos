
# http://www.geeksforgeeks.org/merge-k-sorted-linked-lists/
inp = [
    [1,3,5,7],
    [2,4,6,8],
    [0,9,10,11]
]



class Node:

    def __init__(self, value, link=None, index=1):
        self.value = value
        self.link = link
        self.index = index

    def __str__(self):
        space = ' ' * ((self.index+1) * 1)
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


inp_lls = [genll(a) for a in inp]


def merge(base, extras):
    base_pointer = base

    for extra in extras:
        prev_base = None
        base = base_pointer

        while extra:
            print "IS greater ", base.value, '>=', extra.value
            if base.value >= extra.value:
                print 'Yess'
                if prev_base:
                    prev_base, extra = swap_link(prev_base, extra)
                    prev_base, base = base, prev_base.link
                else:
                    print 'firsttime'
                    prev_base = Node(value=extra.value, link=base)
                    extra = extra.link
            else:
                print 'Noo'
                if not prev_base:
                    prev_base, base = base, base.link
                else:
                    prev_base, base = base, base.link

            print '--------------------'
            print 'Prev base = ',prev_base
            print '--------------------'
            print 'Base = ',base
            print '--------------------'
            print 'extra = ', extra
            print ''
            if not base:
                prev_base.link = extra
                print base_pointer
                break



def swap_link(a, b):
    if not a:
        return b
    new_b = b.link
    a.link, b.link = b, a.link
    return a, new_b


print inp_lls[0], inp_lls[1]
print "***" * 10
print merge(inp_lls[0], inp_lls[1:])




