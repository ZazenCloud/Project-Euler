def cycle_length(num):
    while num % 2 == 0:
        num //= 2
    while num % 5 == 0:
        num //= 5
    if num == 1:
        return 0
    remainder = 1
    length = 0
    while True:
        remainder = (remainder * 10) % num
        length += 1
        if remainder == 1:
            return length


def max_cycle_length(limit):
    max_length = 0
    max_d = 0
    for d in range(1, limit):
        len = cycle_length(d)
        if len > max_length:
            max_length = len
            max_d = d
    return max_d, max_length


print(max_cycle_length(1000))
