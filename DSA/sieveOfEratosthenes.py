def sieve_of_eratosthenes(limit):
    primes = []
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    for number in range(2, int(limit**0.5) + 1):
        if is_prime[number]:
            primes.append(number)
            for multiple in range(number * number, limit + 1, number):
                is_prime[multiple] = False

    for number in range(int(limit**0.5) + 1, limit + 1):
        if is_prime[number]:
            primes.append(number)

    return primes


limit = 10
result = sieve_of_eratosthenes(limit)
print(result)
