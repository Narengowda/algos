inp = [1, 4, 20, 3, 10, 5]
s = 33

temp =  0
start = 0
end =0

for x in inp:
    print "temp  =",temp
    if temp == s:
        print "found",start, " end",end
    elif temp > s:
        t = temp
        for x in inp:
            t = t - x
            print "reverse=", t
            if t == s:
                print "sec found",start, " end",end
            start += 1
    temp += x
    end += 1


