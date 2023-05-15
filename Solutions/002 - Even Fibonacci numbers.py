first_num = 1
second_num = 1
even_fib_sum = 0

while second_num < 4000000:
    temp_num = first_num + second_num
    first_num = second_num
    second_num = temp_num
    if second_num % 2 == 0:
        even_fib_sum += second_num

print(even_fib_sum)
