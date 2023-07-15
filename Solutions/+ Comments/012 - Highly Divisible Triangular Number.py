import math


def find_divisors(n):
    """Returns a dictionary of prime factors
    and their exponents for a given number."""
    divisors = {}
    i = 2
    while i <= math.sqrt(n):
        # Check if 'i' is a divisor of 'n'
        if n % i == 0:
            # Increment the exponent of i in the dictionary
            divisors[i] = divisors.get(i, 0) + 1
            # Divide 'n' by 'i'
            n //= i
        # If 'i' is not a divisor of 'n'
        else:
            i += 1
    # If 'n' is still greater than 1 after the loop
    if n > 1:
        # Add 'n' as a prime factor with exponent one
        divisors[n] = divisors.get(n, 0) + 1
    return divisors


def count_divisors(n):
    """Returns the number of divisors for a given
    number using its prime factorization."""
    divisors = find_divisors(n)
    count = 1
    # Loop over the exponents in the dictionary
    for exponent in divisors.values():
        # Multiply the count by (exponent + 1)
        count *= (exponent + 1)
    return count


limit = 500
n = 1
while True:
    # Formula for calculating the n-th triangle number
    triangle = n * (n + 1) // 2
    # Calculate the number of divisors for the triangle number
    divisors = count_divisors(triangle)
    if divisors > limit:
        # Return the answer
        print(triangle)
        break
    else:
        n += 1
