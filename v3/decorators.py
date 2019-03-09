def c(f):
    def inner(*args, **kargs):
        inner.co += 1
        print("--")
        return f(*args, **kargs)

    print("heeeeee")
    inner.co = 0
    return inner


@c
def fnc():
    pass


if __name__ == "__main__":
    fnc()
    fnc()
    fnc()
    print(fnc.co)
