def binary_search(array, target):
    """Search for a target item in an array by division on two each time until element will be founded."""
    left, right = 0, len(array) - 1

    while left <= right:
        mid = left + (right - left) // 2

        # Check if the target is at the mid index
        if array[mid] == target:
            return mid

        # If the target is greater, ignore the left half
        elif array[mid] < target:
            left = mid + 1

        # If the target is smaller, ignore the right half
        else:
            right = mid - 1

    # If the target is not found in the array
    return -1


# Example
array = [1, 144, 3, 5, 7, 9, 11, 13, 15]
target = 7

array.sort()

result = binary_search(array, target)
print(result)

