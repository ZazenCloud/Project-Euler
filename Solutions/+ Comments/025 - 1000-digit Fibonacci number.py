# First two Fibonacci numbers
first_num = 1
second_num = 1
# Index of the current Fibonacci number
index = 2
fib_num = 0

# Calculate Fibonacci numbers until the length of the current number is at least 1000 digits
while len(str(fib_num)) < 1000:
    fib_num = first_num + second_num
    # Update the values for the next iteration
    first_num = second_num
    second_num = fib_num
    # Increment the index
    index += 1

print(index)
