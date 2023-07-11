def sieve(num):
    """Generates all primes below 'num' using a sieve algorithm."""
    # List of booleans to mark the numbers as prime or not
    is_prime = [True] * num
    # Mark 0 and 1 as not prime
    is_prime[0] = is_prime[1] = False
    # Loop over the numbers from 2 to sqrt(n)
    for i in range(2, int(num**0.5) + 1):
        # If the number is marked as prime, mark its multiples as not prime
        if is_prime[i]:
            for j in range(i * i, num, i):
                is_prime[j] = False
    return [i for i in range(num) if is_prime[i]]


def has_repeats(num):
    """Checks if a number has at least three
    repeated digits in the same positions."""
    num_string = str(num)
    for digit in range(10):
        # Count how many times the digit appears in the string
        count = num_string.count(str(digit))
        # If the count is at least 3, return True
        if count >= 3:
            return True
    return False


def replace_and_check(num, primes):
    """Replaces the repeated digits in a number
    with another digit and checks if it is prime."""
    num_string = str(num)
    count = 0
    # Check all digits (0-9)
    for digit in range(10):
        # Replace the repeated digits with the new digit
        new = num_string.replace(num_string[0], str(digit))
        # Convert the string back to an integer
        new_string = int(new)
        # If the number is prime and has the same length
        # as the original number, increment the counter
        if new_string in primes and len(str(new_string)) == len(num_string):
            count += 1
    return count


primes = sieve(1000000)
max_count = 0
smallest_prime = None

for prime in primes:
    # If the prime has at least three repeated digits
    if has_repeats(prime):
        # Replace and check for primes
        count = replace_and_check(prime, primes)
        # Update values as needed
        if count > max_count:
            max_count = count
            smallest_prime = prime

print(smallest_prime)
