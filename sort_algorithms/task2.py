def merge_sort(array):
    def _merge_sort(array, start, end):
        if start < end:
            mid = (start + end) // 2
            _merge_sort(array, start, mid)
            _merge_sort(array, mid + 1, end)
            _merge(array, start, mid, end)

    def _merge(array, start, mid, end):
        left_size = mid - start + 1
        right_size = end - mid

        left = [0] * left_size
        right = [0] * right_size

        for i in range(left_size):
            left[i] = array[start + i]
        for j in range(right_size):
            right[j] = array[mid + 1 + j]

        i = 0
        j = 0
        k = start

        while i < left_size and j < right_size:
            if left[i] <= right[j]:
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j]
                j += 1
            k += 1

        while i < left_size:
            array[k] = left[i]
            i += 1
            k += 1

        while j < right_size:
            array[k] = right[j]
            j += 1
            k += 1

    _merge_sort(array, 0, len(array) - 1)
    return array


if __name__ == "__main__":
    arr = [38, 27, 43, 3, 9, 82, 10]
    print("Original array:", arr)
    sorted_arr = merge_sort(arr)
    print("Sorted array:", sorted_arr)
