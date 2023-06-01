target_sum = 1000

for a in range(1, target_sum):
    for b in range(a + 1, target_sum):
        c = target_sum - a - b
        if a**2 + b**2 == c**2:
            print(a * b * c)
            break
    else:
        continue
    break