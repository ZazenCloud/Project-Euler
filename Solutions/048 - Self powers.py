total = 0

for num in range(1, 1001):
    expo_num = num ** num
    total += expo_num
    
print(str(total)[-10:])