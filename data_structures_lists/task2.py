class Node:
    """Node class for a singly linked list."""
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    """Stack implementation using a singly linked list."""
    def __init__(self):
        self.top = None
        self.size = 0

    def is_empty(self):
        """Check if the stack is empty."""
        return self.top is None

    def push(self, data):
        """Push an element onto the stack."""
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        self.size += 1

    def pop(self):
        """Pop an element from the stack."""
        if self.is_empty():
            raise IndexError("Pop from an empty stack")
        popped_data = self.top.data
        self.top = self.top.next
        self.size -= 1
        return popped_data

    def peek(self):
        """Return the element at the top of the stack without removing it."""
        if self.is_empty():
            raise IndexError("Peek from an empty stack")
        return self.top.data

    def __len__(self):
        """Return the number of elements in the stack."""
        return self.size

    def __str__(self):
        """Return a string representation of the stack."""
        if self.is_empty():
            return "Stack is empty"
        current = self.top
        stack_str = "Top -> "
        while current:
            stack_str += str(current.data) + " -> "
            current = current.next
        stack_str += "None"
        return stack_str

if __name__ == "__main__":
    stack = Stack()

    stack.push(10)
    stack.push(20)
    stack.push(30)
    print("Stack after pushes:")
    print(stack)

    print("Peek:", stack.peek())

    print("Popped:", stack.pop())
    print("Stack after pop:")
    print(stack)

    print("Stack size:", len(stack))

    print("Popped:", stack.pop())
    print("Popped:", stack.pop())

    print("Is stack empty?", stack.is_empty())

    try:
        stack.pop()
    except IndexError as error:
        print(error)
