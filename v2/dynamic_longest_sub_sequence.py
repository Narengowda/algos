# Longest increasing subsequence


d = [3,2,6,4,5,1]


def LIS(d):
    L = []
    for i in range(0, len(d)):

        # initialize [[]] so that max() wont complaint empty sequence error
        temp = [[]]
        for j in range(i):

            # Compare Result[-1] from 0 to i in L
            if (L[j][-1] < d[i]):
                # append the Previous computed result itself
                temp.append(L[j])

        # just reverse :D :D when they are same priority goes to last one
        temp = temp[::-1]

        # Get max length result among previous results and add current (i)'s value
        L.append(max(temp, key=len) + [d[i]])

    return L

print LIS(d)

# output [[3], [2], [2, 6], [2, 4], [2, 4, 5], [1]]
