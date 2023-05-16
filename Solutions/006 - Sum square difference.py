sum_of_squares = 0
square_of_sums = 0

for num in range(1, 101):
    result = num * num
    sum_of_squares += result

for num in range(1, 101):
    square_of_sums += num

square_of_sums = square_of_sums * square_of_sums

print(square_of_sums - sum_of_squares)
