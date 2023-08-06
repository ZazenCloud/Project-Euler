def sum_of_proper_divisors(n):
    proper_divisors_sum = 1
    for divisor in range(2, int(n**0.5) + 1):
        if n % divisor == 0:
            proper_divisors_sum += divisor
            if divisor != n // divisor:
                proper_divisors_sum += n // divisor
    return proper_divisors_sum


sum_amicables = 0
amicable_set = set()

for num in range(1, 10000):
    if num not in amicable_set:
        calculating_sum = sum_of_proper_divisors(num)
        if calculating_sum != num and sum_of_proper_divisors(calculating_sum) == num:
            sum_amicables += num + calculating_sum
            amicable_set.add(num)
            amicable_set.add(calculating_sum)
print(sum_amicables)
