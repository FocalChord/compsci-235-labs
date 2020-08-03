def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)


def iter_fib(n):
    first = 0
    second = 1
    while first < n:
        first, second = first + second, first
    return first


print(iter_fib(6))
