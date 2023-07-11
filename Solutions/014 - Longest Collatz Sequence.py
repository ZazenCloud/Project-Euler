num = 1
max_chain = 0
target = 0

while num < 1000000:
    next_num = num
    chain = 0
    while next_num != 1:
        if next_num % 2 == 0:
            next_num = next_num / 2
        else:
            next_num = next_num * 3 + 1
        chain += 1
    if chain > max_chain:
        max_chain = chain
        target = num
    num += 1

print(target)
