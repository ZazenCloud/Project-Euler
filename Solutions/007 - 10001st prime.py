num = 2
prime_counting = 1

while prime_counting <= 10001:
    is_not_prime = 0
    for j in range(2, num):
        if (num % j == 0):
            is_not_prime = 1
            break
    if is_not_prime == 1:
        pass
    else:
        print(prime_counting, num)
        prime_counting += 1
    num += 1
