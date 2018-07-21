class Node(object):

    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def gen_ll(arr):
    prev = None
    start = None
    for i in arr:
        n = Node(i)
        if prev:
            prev.next = n

        prev = n

        if not start:
            start = n
    return start


fist_ll = gen_ll([9, 4, 6])
sec_ll = gen_ll([8, 4])


def mul_ll(fist_ll, sec_ll):



