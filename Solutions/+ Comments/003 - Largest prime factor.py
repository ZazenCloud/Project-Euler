# Define a function that finds all prime factors of a given number
def prime_factors(num):
    # Initialize an empty list to store the prime factors
    factors = []
    # Start checking for prime factors at 2
    i = 2
    # Continue checking until the number is completely factored
    while i <= num:
        # If the current number is a factor of the input
        # Add it to the list of factors
        if num % i == 0:
            factors.append(i)
            # Divide the input by the factor to reduce it
            num /= i
        else:
            # If the current number is not a factor, move on to the next one
            i += 1
    # Return the list of prime factors
    return factors


# Find the largest prime factor of 600851475143 and print it
biggest_prime_factor = max(prime_factors(600851475143))
print(biggest_prime_factor)
