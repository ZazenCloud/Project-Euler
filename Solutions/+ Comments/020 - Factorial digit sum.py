n = 100
fact = 1

# Calculate the factorial of n
for i in range(1, n+1):
    fact = fact * i

# Convert the factorial to a list of individual digits
list_of_ints = [int(x) for x in str(fact)]
# Calculate the factorial of n
result = sum(list_of_ints)
print(result)