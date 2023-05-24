# 2 raised to the power of 1000 converted to a string
num = str(2 ** 1000)
# Each character in the string converted to an integer and stored in a list
list_of_ints = [int(x) for x in num]
# Sum of the integers in the list
result = sum(list_of_ints)
print(result)
