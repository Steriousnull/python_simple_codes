from itertools import combinations_with_replacement

# Define the list and the combination length
a = [1, 2, 3, 4, 5, 6, 7, 8]
n = 5

# Generate combinations
combinations = combinations_with_replacement(a, n)

# Print the combinations
for comb in combinations:
    print(comb)
