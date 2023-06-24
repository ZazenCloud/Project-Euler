def count_partitions(n):
    # Create a list to store the partition counts for each number from 0 to n
    partitions = [0] * (n + 1)

    partitions[0] = 1

    # Iterate over all possible numbers to consider them as potential partitions
    for i in range(1, n):
        # Update the partition counts for each number j from i to n
        for j in range(i, n + 1):
            # Add the number of partitions obtained by subtracting i from the current number j
            # to the existing count of partitions for number j
            partitions[j] += partitions[j - i]

    # Return the number of partitions for the given number n
    return partitions[n]

# Calculate the number of different ways to write 100 as a sum of at least two positive integers
num_partitions = count_partitions(100)
print(num_partitions)
