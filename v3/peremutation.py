def perm(nums):
    out = []

    if len(nums) == 1:
        return [nums]

    for i in range(len(nums)):
        inp = nums[0:i] + nums[i + 1 :]
        temp_out = perm(inp)
        temp_out = [[nums[i]] + to for to in temp_out]
        out += temp_out

    return out


print(perm([1, 2, 3]))
