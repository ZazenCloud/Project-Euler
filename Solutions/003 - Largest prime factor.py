def prime_factors(num):
    factors = []
    i = 2
    while i <= num:
        if num % i == 0:
            factors.append(i)
            num /= i
        else:
            i += 1
    return factors


biggest_prime_factor = max(prime_factors(600851475143))
print(biggest_prime_factor)
