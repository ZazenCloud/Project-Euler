def sum_of_proper_divisors(n):
    """Returns the sum of the proper divisors of a number."""
    # Initialize the sum to 1, since 1 is always a divisor
    proper_divisors_sum = 1
    # Loop from 2 to the square root of n
    for divisor in range(2, int(n**0.5) + 1):
        # If i is a divisor of n
        if n % divisor == 0:
            # Add i to the sum
            proper_divisors_sum += divisor
            # If i is not the square root of n
            if divisor != n // divisor:
                # Add the corresponding divisor
                proper_divisors_sum += n // divisor
    return proper_divisors_sum


sum_amicables = 0
amicable_set = set()

# Loop from 1 to 9999
for num in range(1, 10000):
    # If num is not in the amicable numbers set
    if num not in amicable_set:
        # Calculate the sum of the proper divisors of num
        calculating_sum = sum_of_proper_divisors(num)
        # If calculating_sum is not equal to num and the sum of
        # the proper divisors of calculating_sum is equal to num
        if calculating_sum != num and sum_of_proper_divisors(calculating_sum) == num:
            # Add both num and calculating_sum to the 
            # total sum and to the set of amicable numbers
            sum_amicables += num + calculating_sum
            amicable_set.add(num)
            amicable_set.add(calculating_sum)
print(sum_amicables)
