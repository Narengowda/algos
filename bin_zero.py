inp = '010111000101011101101100100100011110'


one_pos = 0
zero_pos = 0
prev_zero_pos = 0

start = 0
end = 0

found_zero = 0
init = True
data = ''
print inp

print '*'*20

while end < len(inp):
    cur = int(inp[end])
    # print cur, start, end

    if cur == 0:
        found_zero += 1
        prev_zero_pos = zero_pos
        zero_pos = end
    else:
        one_pos = end

    if cur == 0 and found_zero > 1:
        # print start,end,'>>>'
        start_i = start+1 if not init else start
        init = False
        print inp[start_i:end]
        start = prev_zero_pos
        found_zero = 1

    end += 1

