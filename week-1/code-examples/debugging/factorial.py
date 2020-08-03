def factorial(n):
    val = 1
    for i in range(1, n + 1):
        val *= i
    return val


print(factorial(5))
