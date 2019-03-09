x = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

max_so_far = x[1]

max_now = x[0]

for i in x[1:]:

    max_now = max(max_now + i, i)

    max_so_far = max(max_so_far, max_now)

print(max_so_far)
