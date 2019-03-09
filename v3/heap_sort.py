import operator
import math


class Heap(object):
    def __init__(self, values, op):
        self.values = values if values else []
        self.op = op

    def insert(self, value):
        self.values.append(value)
        self._heapify()

    def _heapify(self, index=0):
        c_one, c_two = self.children(index)

        if c_one:
            self._heapify(c_one)
            if self.op(self.values[c_one], self.values[index]):
                self.values[index], self.values[c_one] = self.values[c_one], self.values[index]

        if c_two:
            self._heapify(c_two)
            if self.op(self.values[c_two], self.values[index]):
                self.values[index], self.values[c_two] = self.values[c_two], self.values[index]


    def children(self, parent_index):
        one, two = parent_index * 2 + 0, parent_index * 2 + 1
        if one >= len(self.values):
            one = None
        if two >= len(self.values):
            two = None
        return one, two

    def parent(self, children_index):
        return math.ceil(children_index / 2)

    def pop(self):
        max_ele = self.values[0]
        del self.values[0]
        self._heapify()
        return max_ele

    def sort(self):
        for i in range(len(self.values) + 1000):
            self._heapify()




heap = Heap([6,3,2,8,4,2,65,22,2,224,7,9], operator.gt)
heap.sort()


print heap.values

