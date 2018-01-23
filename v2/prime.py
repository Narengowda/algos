
num = 100

i = 0

primes = []

cp = 0

while cp < num:
    print('=====i {}'.format(i))
    i += 1

    if i == 1 or i == 2 or i == 5 or i==3:
        primes.append(i)
        print(i)
        cp = i
        continue

    if not(i % 2 or i % 5):
        primes.append(i)
        cp = i
        print(i)

