largest_palindrome = 0

# Loop through all 3-digit numbers
for i in range(100, 1000):
    for j in range(100, 1000):
        # Calculate the product of the two numbers
        product = i * j

        # Check if the product is a palindrome
        # And if it's greater than the current largest palindrome
        if str(product) == str(product)[::-1] and product > largest_palindrome:
            # If so, update the largest palindrome
            largest_palindrome = product

# Print the largest palindrome
print(largest_palindrome)
