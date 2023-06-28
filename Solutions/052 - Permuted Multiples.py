def check_digits(n1, n2):
    return sorted(str(n1)) == sorted(str(n2))


num = 1
found = False

while not found:
    if all(check_digits(num, i*num) for i in range(2, 7)):
        found = True
    else:
        num += 1

print(num)
