"""
Let us say that you are given a number N, you've to find the number of different ways to write it as the sum of 1, 3 and 4.

For example, if N = 5, the answer would be 6.

    1 + 1 + 1 + 1 + 1
    1 + 4
    4 + 1
    1 + 1 + 3
    1 + 3 + 1
    3 + 1 + 1

"""
literals = [1, 3, 4]
N = 5

C = 0

cache = {}

key = "{}-{}".format


def comb(prev_sum):
    global C
    if prev_sum == N:
        C += 1
        return
    if prev_sum > N:
        return

    for i in literals:
        comb(prev_sum + i)


comb(0)
print(C)
