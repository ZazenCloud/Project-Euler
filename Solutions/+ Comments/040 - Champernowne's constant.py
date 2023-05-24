# Number string with "0." to represent a decimal fraction
num = "0."
# Starting value for appending to the number string
n = 1

# Append consecutive integers to the number string until it reaches 1 million decimals
while (len(num) - 2) < 1000000:
    num += str(n)
    n += 1

# The 2nd index of num is d1 (first digit of the fraction part), the 11th index is d10 and so on...
result = int(num[2]) * int(num[11]) * int(num[101]) * int(num[1001]) * int(num[10001]) * int(num[100001]) * int(num[1000001])
print(result)
