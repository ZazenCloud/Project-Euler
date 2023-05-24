first_num = 1
second_num = 1
index = 2
fib_num = 0

while len(str(fib_num)) < 1000:
    fib_num = first_num + second_num
    first_num = second_num
    second_num = fib_num
    index += 1

print(index)
