def in_range(start, end, step=1):
    while start <= end:
        yield start
        start += step


print(list(in_range(1, 10, 3)))

