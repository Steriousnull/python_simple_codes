import itertools

# Define the digits
digits = [1, 2, 3, 4, 5, 6, 7, 8]

# Generate all possible 5-number combinations
combinations = itertools.permutations(digits, 5)

# Open a file to write the output
with open('combinations_outputs8.txt', 'w') as file:
    # Write each combination to the file
    for combination in combinations:
        file.write(str(combination) + '\n')

print("Combinations have been saved to 'combinations_outputs8.txt'")
