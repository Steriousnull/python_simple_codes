# Example array (list) in Python
array = [10, 20, 30, 40, 50]

# Function to access index and perform operations
def perform_operations(arr):
    for index in range(len(arr)):
        # Accessing the element using the index
        element = arr[index]
        
        # Example operation: doubling the element
        doubled_value = element * 2
        
        # Printing the index, original element, and result of the operation
        print(f"Index: {index}, Element: {element}, Doubled: {doubled_value}")

# Calling the function with the example array
perform_operations(array)



'''    OUTPUT

Index: 0, Element: 10, Doubled: 20
Index: 1, Element: 20, Doubled: 40
Index: 2, Element: 30, Doubled: 60
Index: 3, Element: 40, Doubled: 80
Index: 4, Element: 50, Doubled: 100  '''
