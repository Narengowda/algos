def ackermann(m, n):
    """
    This is the efficient way to execute ackermann function.
    Recursion with memoisation will also cause to either memeory overflow
    or max recursion error

    n+1                 if m=0
    a(m-1, 1)           if m>0 and n=0
    a(m-1, a(m, n-1))   if m>0 and n>0
    """
    if not (isinstance(m, int) and m >= 0):
        raise ValueError("Parameter m is invalid")

    if not (isinstance(n, int) and n >= 0):
        raise ValueError("Parameter n is invalid")

    stack = []
    while m or stack:

        # if m=0
        if not m:
            m, n = stack.pop(), n + 1
        # if m>0 and n=0
        elif not n:
            m, n = m - 1, 1
        # if m>0 and n>0
        else:
            stack.append(m - 1)
            n -= 1

    # handle when m=0
    return n + 1


print(ackermann_peter_10(2, 6))
