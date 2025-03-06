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

    def peek(self):
        """Return the item at the top of the stack without removing it."""
        if not self.is_empty():
            return self.items[-1]
        else:
            return None

def is_balanced(sequence):
    """Check if the sequence of parentheses, braces, and curly brackets is balanced."""
    stack = Stack()
    matching_pairs = {')': '(', '}': '{', ']': '['}

    for char in sequence:
        if char in matching_pairs.values():
            stack.push(char)

        elif char in matching_pairs.keys():
            if stack.is_empty() or stack.peek() != matching_pairs[char]:
                return False
            stack.pop()

    return stack.is_empty()


if __name__ == "__main__":
    sequence = input("Enter a sequence of characters: ")

    if is_balanced(sequence):
        print("The sequence is balanced.")
    else:
        print("The sequence is not balanced.")
