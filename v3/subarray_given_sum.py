# https://practice.geeksforgeeks.org/problems/subarray-with-given-sum/0

x = [10, 2, 13, 4, 5, 16, 7, 8, 9, 10]

s = 0
e = 0

search = 32

while e < len(x):
    if sum(x[s:e]) == search:
        print("found", x[s:e])
        break
    elif sum(x[s:e]) > search:
        s = s+1
    else:
        e = e+1
