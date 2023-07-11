num = 1
max_chain = 0
target = 0

while num < 1000000:
    next_num = num
    chain = 0
    # Calculate the chain until reaching 1
    while next_num != 1:
        # If the number is even
        if next_num % 2 == 0:
            next_num = next_num / 2
        # If the number is odd
        else:
            next_num = next_num * 3 + 1
        chain += 1
    # If the current chain is longer than the previous maximum
    if chain > max_chain:
        max_chain = chain
        target = num
    # Move to the next number
    num += 1

print(target)
