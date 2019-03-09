x = "thisisbigbangtheory"

print(len(x))

temp = {}
max_so_far = 0

for i in x:
    print(i, max_so_far)
    if temp.get(i):
        print("max_so_far", max_so_far)
        max_so_far = 0
        temp = {}
    else:
        temp[i] = 1
        max_so_far += 1

print max_so_far
