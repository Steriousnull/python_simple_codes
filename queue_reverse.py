from queue import Queue

def reverse_queue(q):
    stack = []
    
    # Dequeue all elements of the queue and push them onto the stack
    while not q.empty():
        stack.append(q.get())
    
    # Pop all elements from the stack and enqueue them back to the queue
    while stack:
        q.put(stack.pop())

# Initialize the queue
q = Queue()

# Get input from the user for 5 digits
print("Enter 5 digits:")

original_list = []
for _ in range(5):
    digit = int(input("Enter digit: "))
    q.put(digit)
    original_list.append(digit)

# Print the original order of the queue
print("Original Queue:", original_list)

# Reverse the queue
reverse_queue(q)

# Print the reversed queue
reversed_list = []
while not q.empty():
    reversed_list.append(q.get())

print("Reversed Queue:", reversed_list)


'''
Enter 5 digits:
Enter digit: 1
Enter digit: 4
Enter digit: 6
Enter digit: 2
Enter digit: 8
Original Queue: [1, 4, 6, 2, 8]
Reversed Queue: [8, 2, 6, 4, 1]
'''
