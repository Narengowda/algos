i = 5
while True:
    # 0o is octal allowed only up to 7
    if i % 0o8 == 0:
        break
    print(i)
    i += 1
