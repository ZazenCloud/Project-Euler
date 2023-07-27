def num_prime_factors(n):
    """ Returns the number of distinct prime factors of n."""
    i = 2
    # A set is used to avoid counting repeated factors
    factors = set()
    while i * i <= n:
        if n % i == 0:
            # Add i to the set of factors
            factors.add(i)
            # Divides n by i
            n //= i
        else:
            i += 1
    if n > 1:
        # Adds the remaining factor to the set
        factors.add(n)
    # Returns the size of the set
    return len(factors)


count = 0
answer = 0
n = 2

while True:
    # If n has four distinct prime factors
    if num_prime_factors(n) == 4:
        # Increment count by 1
        count += 1
        # If this is the first integer in the sequence
        if count == 1:
            answer = n
        # If four consecutive integers are found
        if count == 4:
            print(answer)
            break
    # If n does not have four distinct prime factors
    else:
        count = 0
        first = 0
    n += 1
