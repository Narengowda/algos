import time
x = [2,3,6,7,9]
y = [1,4,8,10]

main = []
while len(x) != 0 and len(y) != 0:
    xe = x[0]
    ye = y[0]

    print xe,ye
    if xe and ye:
        if (xe <= ye):
            main.append(xe)
            x = x[1:]
        else:
            main.append(ye)
            y = y[1:]

    else:
        main = main + x + y
        break
print main


