import itertools

# Define the digits
digits = [1, 2, 3, 4, 5]

# Generate all possible 5-number combinations
combinations = itertools.permutations(digits, 5)

# Print each combination
for combination in combinations:
    print(combination)
