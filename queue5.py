from collections import deque

# Initialize a queue
queue = deque()

# Taking input of 5 values
print("Enter 5 values to add to the queue:")
for _ in range(5):
    value = int(input())
    queue.append(value)  # Enqueue operation

# Displaying the queue
print("Queue elements are:")
print(list(queue))

# Dequeue operation: Removing elements from the queue
print("\nDequeueing all elements:")
while queue:
    dequeued_value = queue.popleft()
    print("Dequeued:", dequeued_value)

if not queue:
    print("Queue is empty now!")
