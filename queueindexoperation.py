from collections import deque

# Initialize a queue
queue = deque()

# Taking input of 5 values
print("Enter 5 values to add to the queue:")
for _ in range(5):
    value = int(input())
    queue.append(value)  # Enqueue operation

# Accessing the index and element in the queue
print("\nQueue elements with their indices:")
for index, value in enumerate(queue):
    print(f"Index {index}: {value}")

# Performing an operation on an element at a specific index
# Example: Doubling the value at index 2
index_to_modify = 2
if index_to_modify < len(queue):
    queue[index_to_modify] *= 2
    print(f"\nAfter modifying element at index {index_to_modify}:")
    print(list(queue))
else:
    print(f"\nIndex {index_to_modify} is out of bounds.")
