num_list = []

for i in range(2, 101):
    for j in range(2, 101):
        num = j ** i
        num_list.append(num)
unique_numbers = list(set(num_list))
result = len(unique_numbers)
print(result)