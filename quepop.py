from collections import deque

# Initialize a queue with a maximum size of 5
queue = deque()

# Function to add a new element to the queue, ejecting the last element if needed
def add_to_queue(value):
    if len(queue) == 5:
        removed_value = queue.pop()  # Eject the last element
        print(f"Removed last element: {removed_value}")
    queue.appendleft(value)  # Add the new element to the front of the queue
    print(f"Added new element: {value}")

# Taking input of 5 initial values
print("Enter 5 values to add to the queue:")
for _ in range(5):
    value = int(input())
    queue.append(value)  # Enqueue operation

# Displaying the initial queue
print("\nInitial Queue elements:")
print(list(queue))

# Adding a new value and ejecting the last element if necessary
print("\nEnter a new value to add to the queue:")
new_value = int(input())
add_to_queue(new_value)

# Displaying the queue after the operation
print("\nQueue elements after adding new value:")
print(list(queue))
