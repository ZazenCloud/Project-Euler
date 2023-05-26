n = 100
fact = 1

for i in range(1, n+1):
    fact = fact * i

list_of_ints = [int(x) for x in str(fact)]
result = sum(list_of_ints)
print(result)