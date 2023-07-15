import math


def find_divisors(n):
    divisors = {}
    i = 2
    while i <= math.sqrt(n):
        if n % i == 0:
            divisors[i] = divisors.get(i, 0) + 1
            n //= i
        else:
            i += 1
    if n > 1:
        divisors[n] = divisors.get(n, 0) + 1
    return divisors


def count_divisors(n):
    divisors = find_divisors(n)
    count = 1
    for exponent in divisors.values():
        count *= (exponent + 1)
    return count


limit = 500
n = 1
while True:
    triangle = n * (n + 1) // 2
    divisors = count_divisors(triangle)
    if divisors > limit:
        print(triangle)
        break
    else:
        n += 1
