reach = int(raw_input('Enter max number\n') or 1000)

print "For reach"

def steps(seed, reach):
    last = seed % 10

    if last == 0:
        a = int(str(seed) + '1')
        b = None
    else:
        a = int(str(seed) + str(last+1))
        b = int(str(seed) + str(last-1))

    # print a,b
    if a and (a < reach):
        dataa = [a]
        dataa.extend(steps(a, reach))
    else:
        dataa = []

    if b and (b < reach):
        datab = [b]
        datab.extend(steps(b, reach))
    else:
        datab = []

    return dataa + datab

print sorted(reduce(lambda x,y: x+y, [steps(i, reach) for i in range(10)]))
