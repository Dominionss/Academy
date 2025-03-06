import random

def quicksort(array, partition_limit=10):
    def _quicksort(array, low, high):
        if low < high:
            if high - low + 1 <= partition_limit:
                insertion_sort(array, low, high)
            else:
                pivot_index = partition(array, low, high)
                _quicksort(array, low, pivot_index - 1)
                _quicksort(array, pivot_index + 1, high)

    def partition(array, low, high):
        pivot = array[high]
        i = low - 1

        for j in range(low, high):
            if array[j] <= pivot:
                i += 1
                array[i], array[j] = array[j], array[i]  # Swap

        array[i + 1], array[high] = array[high], array[i + 1]
        return i + 1

    def insertion_sort(array, low, high):
        for i in range(low + 1, high + 1):
            key = array[i]
            j = i - 1
            while j >= low and array[j] > key:
                array[j + 1] = array[j]
                j -= 1
            array[j + 1] = key

    _quicksort(array, 0, len(array) - 1)
    return array


if __name__ == "__main__":
    arr = [random.randint(1, 100) for _ in range(20)]
    print("Original array:", arr)

    sorted_arr = quicksort(arr)
    print("Sorted array:", sorted_arr)
