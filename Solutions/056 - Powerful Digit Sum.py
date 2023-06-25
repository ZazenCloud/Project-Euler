max_digital_sum = 0

for a in range(1, 100):
    for b in range(1, 100):
        number = a ** b
        digit_sum = sum(int(digit) for digit in str(number))
        if digit_sum > max_digital_sum:
            max_digital_sum = digit_sum

print(max_digital_sum)
