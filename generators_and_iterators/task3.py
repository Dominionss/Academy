class MyList:
    def __init__(self, items=None):
        self.data = items if items else []

    def __getitem__(self, index):
        return self.data[index]  # Enables indexing (e.g., obj[0])

    def __setitem__(self, index, value):
        self.data[index] = value  # Enables item assignment (e.g., obj[0] = 10)

    def __delitem__(self, index):
        del self.data[index]  # Enables deletion (e.g., del obj[0])

    def __len__(self):
        return len(self.data)  # Enables len(obj)

    def __iter__(self):
        return iter(self.data)  # Enables iteration (for x in obj)

    def __contains__(self, item):
        return item in self.data  # Enables 'in' keyword (e.g., 10 in obj)

    def append(self, value):
        self.data.append(value)  # Custom append method

    def __repr__(self):
        return f"{self.data}"  # String representation


if __name__ == "__main__":
    obj = MyList([1, 2, 3])
    print(obj[1])      # Output: 2 (getitem)
    obj[1] = 10        # Modifies index 1
    print(obj)         # Output: [1, 10, 3]
    obj.append(4)      # Appends 4
    print(len(obj))    # Output: 4
    print(10 in obj)   # Output: True
    for i in obj:
        print(i)       # Output: 1, 10, 3, 4

