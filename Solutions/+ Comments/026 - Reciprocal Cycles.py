def cycle_length(num):
    # Remove any factors of 2 and 5 from num
    while num % 2 == 0:
        num //= 2
    while num % 5 == 0:
        num //= 5
    # If num is 1, there is no cycle
    if num == 1:
        return 0
    remainder = 1
    length = 0
    # Loop until the remainder is 1 again
    while True:
        # Multiply the remainder by 10 and take the modulo num
        remainder = (remainder * 10) % num
        # Increment the length
        length += 1
        # If the remainder is 1, the cycle was found
        if remainder == 1:
            return length


def max_cycle_length(limit):
    max_length = 0
    max_d = 0
    # Loop over all possible d from 1 to limit - 1
    for d in range(1, limit):
        # Compute the cycle length of 1 / d
        len = cycle_length(d)
        # If it is greater than the current maximum, update it
        if len > max_length:
            max_length = len
            max_d = d
    return max_d, max_length


print(max_cycle_length(1000))
