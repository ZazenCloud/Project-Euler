exponent = 7830457
base = 2
modulo = 10**10

# Calculate using modular exponentiation
result = pow(base, exponent, modulo)
result = (28433 * result + 1) % modulo

print(result)