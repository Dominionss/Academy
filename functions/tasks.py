def check_locals():
    local_var = 0
    print(locals())


def use_another_function():
    return check_locals


def choose_func(nums: list, func1, func2):
    if all(x >= 0 for x in nums):
        nums = func1(nums)
    else:
        nums = func2(nums)
    return nums


# Tests

nums1 = [1, 2, 3, 4, 5]

nums2 = [1, -2, 3, -4, 5]


def square_nums(nums):
    return [num ** 2 for num in nums]


def remove_negatives(nums):
    return [num for num in nums if num > 0]


# Tests

check_locals()
another_function = use_another_function()
another_function()

print(choose_func(nums1, square_nums, remove_negatives))
print(choose_func(nums2, square_nums, remove_negatives))
