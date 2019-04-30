""" Efficient calculation of factorials"""


def is_even(n):
    return n % 2 == 0


def efficient_factorial(n):
    """
    This method of calculating the factorial by reducing the multiplications by half.
    As we know multiplication is the costlier operation redcing it by half adds a lot of
    performace benifits

    Example:
    8! = 8 * (8 + 6 = 14) * (14 + 4 = 18) * (18 + 2 = 20)
    8! = 8 * 14 * 18 * 20
    8! = 40320

    Explanation here: https://sites.google.com/site/examath/research/factorials

    """
    factorial = 1
    start = n

    if n in [1, 0]:
        return factorial

    # Alwasy make number starts from even number
    if not is_even(n):
        start = n - 1

    temp_sum = start - 2
    factorial = start

    while temp_sum >= 2:

        start = start + temp_sum
        factorial = factorial * start

        temp_sum = temp_sum - 2

    # If the given number is even handle it in the end
    if not is_even(n):
        factorial *= n

    return factorial


print(efficient_factorial(700))
