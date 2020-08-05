def factorial(n):
    val = 1
    for i in range(1, n):
        val *= i
    return val


print(factorial(5))
