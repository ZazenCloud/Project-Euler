# Define the target sum
target_sum = 1000

# Loop through possible values of a
for a in range(1, target_sum):
    # Loop through possible values of b
    for b in range(a + 1, target_sum):
        # Calculate c
        c = target_sum - a - b
        # Check if it is a Pythagorean triplet
        if a**2 + b**2 == c**2:
            # Print the product of the triplet
            print(a * b * c)
            break
    else:
        continue
    break