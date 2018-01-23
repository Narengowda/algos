inp = [-2, 1, -3, -4, -3, 2, 1, -5, 4]

max_sum = [inp[0]]
sum_sofar = [inp[0]]

for i in inp[1:]:
    # print ("{} < {}".format(sum(sum_sofar[::] + [i]), i))

    if sum(sum_sofar[::] + [i]) < i:
        sum_sofar = [i]
    else:
        sum_sofar.append(i)

    if sum(max_sum) < sum(sum_sofar):
        max_sum = sum_sofar[::]


    # print(">>>ssf>>> {}".format(sum_sofar))
    # print(">>>max>>> {}".format(max_sum))
print max_sum


