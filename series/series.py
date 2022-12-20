def fibonacci(n):

    if n == 0:
        return 0

    if n == 1:
        return 1

    if n > 1:
        return fibonacci(n-1)+fibonacci(n-2)


def lucas(n):

    if n == 0:
        return 2

    if n == 1:
        return 1

    if n > 1:
        return lucas(n-1)+lucas(n-2)


def sum_series(n, o=0, p=1):
    """Calling this function with no optional parameters will produce numbers from the fibonacci series. Calling it with the optional arguments 2 and 1 will produce values from the lucas numbers. Other values for the optional parameters will produce other series. Again, you may use recursion or iteration, or both. Again, ensure that your function has a well-formed docstring."""
    if n == 0:
        return o

    if n == 1:
        return p

    if n > p:
        return sum_series(n - 1, o, p) + sum_series(n - 2, o, p)

