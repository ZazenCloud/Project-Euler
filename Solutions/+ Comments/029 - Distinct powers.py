num_list = []

# Iterate over the range of values from 2 to 100 for both variables
for i in range(2, 101):
    for j in range(2, 101):
        # Calculate the power of j to i
        num = j ** i
        # Add the calculated number to the list
        num_list.append(num)  

# Remove duplicates by converting the list to a set and then back to a list
unique_numbers = list(set(num_list))
# Get the count of unique numbers
result = len(unique_numbers)
print(result)
