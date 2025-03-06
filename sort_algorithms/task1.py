def cocktail_shaker_sort(array):
    n = len(array)
    swapped = True
    start = 0
    end = n - 1

    while swapped:
        swapped = False

        for i in range(start, end):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]  # Swap
                swapped = True

        if not swapped:
            break

        swapped = False
        end -= 1

        for i in range(end - 1, start - 1, -1):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]  # Swap
                swapped = True

        start += 1

    return array


if __name__ == "__main__":
    arr = [5, 1, 4, 2, 8, 0, 2]
    print("Original array:", arr)
    sorted_arr = cocktail_shaker_sort(arr)
    print("Sorted array:", sorted_arr)
