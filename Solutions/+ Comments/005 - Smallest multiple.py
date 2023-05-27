import math


def least_common_multiple(a, b):
    # Calculate the LCM of two numbers    
    return abs(a * b) // math.gcd(a, b)


def smallest_evenly_divisible(n):
    # Finds the smallest positive number that is evenly divisible by all numbers from 1 to n
    result = 1
    for i in range(1, n + 1):
        # Update the result by finding the LCM of result and the current number
        result = least_common_multiple(result, i)
    return result


smallest_number = smallest_evenly_divisible(20)
print(smallest_number)
