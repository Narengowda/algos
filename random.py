import time
import psutil
from datetime import datetime
from collections import deque



def gen_random_num(max):
    raw = datetime.now().microsecond
    p = list(str(raw)).pop()
    raw = raw * p

    items = deque(list(str(raw)))
    liitems = list(items)
    items.rotate(-1)
    roitems = list(items)
    bigitems = roitems + liitems
    rooitems = deque(bigitems)
    rooitems.rotate(int(items.pop()))

    penalty = int(rooitems.pop())
    penaltytwo = int(rooitems.popleft())


    for i in range(penalty, penaltytwo):
        if i and int(time.time()) % i:
            rooitems.rotate(int(i))
        else:
            rooitems.rotate(penaltytwo)

    return str(rooitems[int(penalty)])



for i in range(300):
    first = gen_random_num(10)
    second = gen_random_num(10)
    print i, ',', int(first+second)
