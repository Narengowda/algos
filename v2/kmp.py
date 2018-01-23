search = "AABAACAADAABAABA"
pattern = "AABAABAAA"

def gen_pattern_val(pattern):
    j = 0
    res = [0]
    for i in range(1, len(pattern)):
        print("i = {}".format(i))
        print("{} == {}".format(pattern[i], pattern[j]))

        if pattern[i] == pattern[j]:
            print("matched")
            res.append(j+1)
            j += 1
            print("J after increment {} res={}".format(j, res))
        else:
            res.append(0)
            print("didn't matched {}".format(res))
            j = res[j-1]

            if pattern[j] == pattern[i]:
                res.append(j+1)
        print("---------------")
    return res

print(gen_pattern_val(pattern))






