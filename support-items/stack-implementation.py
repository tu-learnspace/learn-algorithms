class Stack:
    def __init__(self):
        # Initialize an empty list to represent the stack.
        self.stack = []

    def isEmpty(self):
        # Check if the stack is empty by comparing it to an empty list.
        return self.stack == []

    def push(self, data):
        # Add the given data to the top of the stack (end of the list).
        self.stack.append(data)

    def pop(self):
        if self.isEmpty():
            # If the stack is empty, return a message indicating so.
            return 'Stack is empty'
        # Remove and return the top element from the stack (last item in the list).
        return self.stack.pop()

    def peek(self):
        if self.isEmpty():
            # If the stack is empty, return a message indicating so.
            return 'Stack is empty'
        # Return the top element from the stack without removing it.
        return self.stack[-1]
