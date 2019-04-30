x = "10000000110"

s = 0
yes = False

for i in x:
    if i == '1':
        yes = True
        s = 0
    elif i == '0':
        s+= 1
        print(s)

