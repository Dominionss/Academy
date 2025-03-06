class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        """Add an item to the top of the stack."""
        self.items.append(item)

    def pop(self):
        """Remove and return the item from the top of the stack."""
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Pop from an empty stack")

    def is_empty(self):
        """Check if the stack is empty."""
        return len(self.items) == 0

def reverse_sequence(sequence):
    """Reverse a sequence of characters using a stack."""
    stack = Stack()

    for char in sequence:
        stack.push(char)

    reversed_sequence = []

    while not stack.is_empty():
        reversed_sequence.append(stack.pop())

    return ''.join(reversed_sequence)

if __name__ == "__main__":
    sequence = input("Enter a sequence of characters: ")
    reversed_sequence = reverse_sequence(sequence)

    print("Reversed sequence:", reversed_sequence)
