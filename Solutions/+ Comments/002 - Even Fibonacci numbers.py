first_num = 1
second_num = 1
even_fib_sum = 0

# Loop until the second number in the sequence exceeds 4 million
while second_num < 4000000:
    # Calculate the next Fibonacci number by summing the previous two
    temp_num = first_num + second_num
    # Shift the values in the sequence over by one
    first_num = second_num
    second_num = temp_num
    # If the current number is even, add it to the sum of even numbers
    if second_num % 2 == 0:
        even_fib_sum += second_num

# Print the sum of even Fibonacci numbers
print(even_fib_sum)
