def num_prime_factors(n):
    i = 2
    factors = set()
    while i * i <= n:
        if n % i == 0:
            factors.add(i)
            n //= i
        else:
            i += 1
    if n > 1:
        factors.add(n)
    return len(factors)


count = 0
answer = 0
n = 2

while True:
    if num_prime_factors(n) == 4:
        count += 1
        if count == 1:
            answer = n
        if count == 4:
            print(answer)
            break
    else:
        count = 0
        first = 0
    n += 1
