arr  = [9.00,  9.40, 9.50,  11.00, 15.00, 18.00]
dep  = [9.10, 12.00, 11.20, 11.30, 19.00, 20.00]

total = 0


# sort them using nlogn

arr.sort()
dep.sort()

arrival = [[x, 'a'] for x in arr]
departure = [[x, 'd'] for x in dep]

max_plat = 0

for i in range(len(arrival) + len(departure) - 2):
    x = arrival[0] if arrival else None
    y = departure[0] if departure else None

    if x and y and x[0] < y[0]:
        if x[1] == 'a':
            total += 1
        else:
            total -= 1
        arrival = arrival[1:]
    elif x[0] > y[0]:
        if y[1] == 'a':
            total += 1
        else:
            total -= 1
        departure = departure[1:]
    elif not x and not y:
        pass
    elif x:
        if x[1] == 'a':
            total += 1
        else:
            total -= 1
    elif y:
        if y[1] == 'a':
            total += 1
        else:
            total -= 1

    if total > max_plat:
        max_plat = total


    print total



print "total plat needed = ",max_plat
