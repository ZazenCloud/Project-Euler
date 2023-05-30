def is_palindromic(n):
    base2 = bin(n)[2:]
    base10 = str(n)
    return base10 == base10[::-1] and base2 == base2[::-1]


def find_sum(limit):
    total = 0
    for n in range(limit):
        if is_palindromic(n):
            total += n
    return total


print(find_sum(1000000))
