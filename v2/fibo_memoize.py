import time


d = {}
def memoize(f):
    def fun(arg):
        if arg in d:
            return d[arg]
        data = f(arg)
        d[arg] = data
        return data

    return fun

@memoize
def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    return fib(n-1) + fib(n-2)


s = time.time()

print(fib(40))

e = time.time()
print(int(e)-int(s))
print(d)































