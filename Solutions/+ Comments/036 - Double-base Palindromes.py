def is_palindromic(n):
    # Convert n to base 10 and base 2 strings
    base10 = str(n)
    base2 = bin(n)[2:]  # Remove the '0b' prefix
    # Check if both strings are equal to their reversed versions
    return base10 == base10[::-1] and base2 == base2[::-1]


def find_sum(limit):
    total = 0
    # Loop through all the numbers less than limit
    for n in range(limit):
        # Check if n is palindromic in both bases
        if is_palindromic(n):
            # Add n to the sum
            total += n
    # Return the sum
    return total


print(find_sum(1000000))
