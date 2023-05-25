total = 0

# Iterate over the numbers from 1 to 1000
for num in range(1, 1001):
    # Calculate the exponentiation of the number raised to itself
    expo_num = num ** num
    # Add the exponentiation result to the total
    total += expo_num

# Print the last 10 digits 
print(str(total)[-10:])