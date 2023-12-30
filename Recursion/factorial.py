def fact(n, accumulator = 1):
    if n == 0 or n == 1:
        return accumulator
    return fact(n-1, n*accumulator)

print(fact(5))