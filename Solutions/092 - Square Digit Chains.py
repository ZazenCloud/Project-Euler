count = 0
memoization = {}


def get_next_number(n):
    '''Calculates the next number in the chain by summing the squares of its digits.'''
    next_number = 0
    while n > 0:
        digit = n % 10
        next_number += digit ** 2
        n //= 10
    return next_number


def calculate_chain(num):
    num = chain
    # Continues calculating the chain until it reaches 1 or 89
    while chain != 1 and chain != 89:
        if chain in memoization:
            # If the chain has been calculated before, retrieve the result from memoization
            chain = memoization[chain]
            break
        chain = get_next_number(chain)
    memoization[num] = chain
    return chain


for num in range(1, 10000000):
    if calculate_chain(num) == 89:
        # If the chain arrives at 89, increment the count
        count += 1

print(count)
