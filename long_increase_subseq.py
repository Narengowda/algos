# not correct

x = [3,4,-1,0,6,2,3]

results = []

n = len(x)

i = 0
j = 1


local_res = []
for i in range(n):
    local_res = []
    last_data = x[i]

    for j in range(i, n):
        if last_data <= x[j]:
            local_res.append(x[j])
            last_data = x[j]

    results.append(local_res)
print(results)
