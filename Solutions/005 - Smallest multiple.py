import math


def least_common_multiple(a, b):
    return abs(a * b) // math.gcd(a, b)


def smallest_evenly_divisible(n):
    result = 1
    for i in range(1, n + 1):
        result = least_common_multiple(result, i)
    return result


smallest_number = smallest_evenly_divisible(20)
print(smallest_number)
