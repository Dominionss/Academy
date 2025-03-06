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

    def get_from_stack(self, e):
        """Search and return an element e from the stack. Raise ValueError if not found."""
        temp_stack = Stack()

        while not self.is_empty():
            item = self.pop()
            if item == e:
                # Restore the stack
                while not temp_stack.is_empty():
                    self.push(temp_stack.pop())
                return e
            else:
                temp_stack.push(item)

        while not temp_stack.is_empty():
            self.push(temp_stack.pop())
        raise ValueError(f"Element {e} not found in the stack")


if __name__ == "__main__":
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)

    try:
        print(stack.get_from_stack(2))  # Output: 2
        print(stack.get_from_stack(4))  # Raises ValueError
    except ValueError as error:
        print(error)
