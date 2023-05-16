sum_of_squares = 0
square_of_sums = 0

# Calculate the sum of squares from 1 to 100
for num in range(1, 101):
    result = num * num
    sum_of_squares += result

# Calculate the square of sums from 1 to 100
for num in range(1, 101):
    square_of_sums += num

square_of_sums = square_of_sums * square_of_sums

# Print the difference between the square of sums and the sum of squares
print(square_of_sums - sum_of_squares)
