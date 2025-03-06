class UnsortedList:
    def __init__(self):
        self.items = []

    def append(self, item):
        """Add an item to the end of the list."""
        self.items.append(item)

    def index(self, item):
        """Return the index of the first occurrence of the item. Raise ValueError if not found."""
        if item in self.items:
            return self.items.index(item)
        else:
            raise ValueError(f"Item {item} not found in the list")

    def pop(self, index=None):
        """Remove and return the item at the given index. If no index is provided, remove and return the last item."""
        if index is None:
            return self.items.pop()
        else:
            return self.items.pop(index)

    def insert(self, index, item):
        """Insert an item at the specified index."""
        self.items.insert(index, item)

    def slice(self, start, stop):
        """Return a copy of the list starting at 'start' and going up to but not including 'stop'."""
        return self.items[start:stop]

    def __str__(self):
        """Return a string representation of the list."""
        return str(self.items)


if __name__ == "__main__":
    ul = UnsortedList()

    ul.append(10)
    ul.append(20)
    ul.append(30)
    print("After append:", ul)

    print("Index of 20:", ul.index(20))

    print("Popped item:", ul.pop(1))
    print("After pop:", ul)

    ul.insert(1, 40)
    print("After insert:", ul)

    # Slice the list
    print("Slice [1:3]:", ul.slice(1, 3))
