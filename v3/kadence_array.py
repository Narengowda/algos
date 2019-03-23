x = [-1, -2, -3, -4]

max_sf = x[:1]
max_now = x[:1]

for i in x:
    if sum(max_now + [i]) > sum([i]):
        max_now = max_now + [i]
    else:
        max_now = [i]

    if sum(max_now) > sum(max_sf):
        max_sf = max_now

print(max_sf)
