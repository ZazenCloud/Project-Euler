def check_digits(n1, n2):
    """Check if two numbers contain the same digits."""
    return sorted(str(n1)) == sorted(str(n2))

num = 1
found = False

while not found:
    if all(check_digits(num, i*num) for i in range(2, 7)):
        # If all numbers 2x, 3x, 4x, 5x, and 6x contain the same digits,
        # set 'found' to True to exit the loop
        found = True
    else:
        # If the digits are not the same, increment num and continue to the next iteration
        num += 1

print(num)
