x = "0 8 4 12 2 10 6 14 1 9 5 13 3 11 7 15"
x = list(map(int, x.split()))

maximum = [[x[0]]]

for i in x[1:]:
    print(i)
    for m in maximum[::]:
        if i >= m[-1]:
            temp_m = m[::]
            temp_m.append(i)
            maximum.append(temp_m)

    maximum.append([i])
    print(maximum)

ll = {len(m): m for m in maximum}

for k, v in ll.items():
    print(k, "  ", v)

print(">> max >>", max(ll.keys()))
print(">> length >>", len(maximum))
print(">> length x >>", len(x))
