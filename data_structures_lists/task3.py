class Node:
    """Node class for a singly linked list."""
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    """Queue implementation using a singly linked list."""
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    def is_empty(self):
        """Check if the queue is empty."""
        return self.front is None

    def enqueue(self, data):
        """Add an element to the rear of the queue."""
        new_node = Node(data)
        if self.is_empty():
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        self.size += 1

    def dequeue(self):
        """Remove and return the element from the front of the queue."""
        if self.is_empty():
            raise IndexError("Dequeue from an empty queue")
        dequeued_data = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        self.size -= 1
        return dequeued_data

    def peek(self):
        """Return the element at the front of the queue without removing it."""
        if self.is_empty():
            raise IndexError("Peek from an empty queue")
        return self.front.data

    def __len__(self):
        """Return the number of elements in the queue."""
        return self.size

    def __str__(self):
        """Return a string representation of the queue."""
        if self.is_empty():
            return "Queue is empty"
        current = self.front
        queue_str = "Front -> "
        while current:
            queue_str += str(current.data) + " -> "
            current = current.next
        queue_str += "None"
        return queue_str


if __name__ == "__main__":
    queue = Queue()
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)

    print("Queue after enqueues:")
    print(queue)

    print("Peek:", queue.peek())

    print("Dequeued:", queue.dequeue())
    print("Queue after dequeue:")
    print(queue)

    print("Queue size:", len(queue))

    print("Dequeued:", queue.dequeue())
    print("Dequeued:", queue.dequeue())

    print("Is queue empty?", queue.is_empty())

    try:
        queue.dequeue()
    except IndexError as error:
        print(error)