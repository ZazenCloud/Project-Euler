sum = 0

# Loop through numbers from 1 to 999
for num in range(1, 1000):
    # If the number is divisible by 3
    # Add it to the sum
    if num % 3 == 0:
        sum += num
    # If the number is not divisible by 3 but is divisible by 5
    # Add it to the sum
    elif num % 5 == 0:
        sum += num

# Print the final sum
print(sum)
