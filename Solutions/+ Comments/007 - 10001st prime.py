num = 2
prime_counting = 1

# Loop until the 10001st prime is found
while prime_counting <= 10001:
    is_not_prime = 0
    # Check if the number is prime
    for j in range(2, num):
        # If the number is divisible by any other number, it's not prime
        if (num % j == 0):
            # Set flag indicating that the number is not prime
            is_not_prime = 1
            # Exit the loop
            break
    if is_not_prime == 1:
        # If the number is not prime, continue to the next number
        pass
    else:
        # If the number is prime, print it and increment the counter
        print(prime_counting, num)
        prime_counting += 1
    # Increment the number to be tested
    num += 1
