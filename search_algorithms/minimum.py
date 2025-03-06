def binary_search_recursive(sorted_array, target, start_index, end_index):
    if start_index > end_index:
        return -1

    middle_index = (start_index + end_index) // 2

    if sorted_array[middle_index] == target:
        return middle_index
    elif sorted_array[middle_index] > target:
        return binary_search_recursive(sorted_array, target, start_index, middle_index - 1)
    else:
        return binary_search_recursive(sorted_array, target, middle_index + 1, end_index)


sorted_array = [1, 3, 5, 7, 9, 11, 13, 15]
target = 7
result = binary_search_recursive(sorted_array, target, 0, len(sorted_array) - 1)
print(f"Element {target} found at index {result}" if result != -1 else "Element not found")

