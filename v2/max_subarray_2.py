# Max sum array
x = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

max_sum = [x[0]]
temp_sum = [x[0]]

for i in x[1:]:

    # If [element] is greater than [temp + element]
    # then temp_sum = [element]
    # else temp_sum = temp_sum + [element]
    if i > sum(temp_sum + [i]):
        temp_sum = [i]
    else:
        temp_sum = temp_sum + [i]


    # if temp is greater the replace with main array
    if sum(temp_sum) > sum(max_sum):
        max_sum = temp_sum[::]

print "------> ", max_sum




