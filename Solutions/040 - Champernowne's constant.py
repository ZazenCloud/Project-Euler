num = "0."
n = 1

while (len(num) - 2) < 1000000:
    num += str(n)
    n += 1

result = int(num[2]) * int(num[11]) * int(num[101]) * int(num[1001]) * int(num[10001]) * int(num[100001]) * int(num[1000001])
print(result)