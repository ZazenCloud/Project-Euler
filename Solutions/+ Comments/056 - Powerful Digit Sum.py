max_digital_sum = 0

# Iterate through all possible values of 'a' from 1 to 99
for a in range(1, 100):
    # Iterate through all possible values of 'b' from 1 to 99
    for b in range(1, 100):
        number = a ** b  
        # Calculate the sum of the digits in 'ab'
        digit_sum = sum(int(digit) for digit in str(number))

        # Check if the current digital sum is greater than the maximum digital sum encountered so far
        if digit_sum > max_digital_sum:
            max_digital_sum = digit_sum

print(max_digital_sum)
