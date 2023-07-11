def sieve(num):
    is_prime = [True] * num
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(num**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, num, i):
                is_prime[j] = False
    return [i for i in range(num) if is_prime[i]]


def has_repeats(num):
    num_string = str(num)
    for digit in range(10):
        count = num_string.count(str(digit))
        if count >= 3:
            return True
    return False


def replace_and_check(num, primes):
    num_string = str(num)
    count = 0
    for digit in range(10):
        new = num_string.replace(num_string[0], str(digit))
        new_string = int(new)
        if new_string in primes and len(str(new_string)) == len(num_string):
            count += 1
    return count


primes = sieve(1000000)
max_count = 0
smallest_prime = None

for prime in primes:
    if has_repeats(prime):
        count = replace_and_check(prime, primes)
        if count > max_count:
            max_count = count
            smallest_prime = prime

print(smallest_prime)
