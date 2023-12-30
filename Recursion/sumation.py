def sumthem(n, accumulator = 1):
    if n == 1: 
        return accumulator
    return sumthem(n-1, n + accumulator)

print(sumthem(5))