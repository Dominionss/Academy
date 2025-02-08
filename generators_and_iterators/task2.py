def in_range(start, end, step=1):
    while start <= end:
        yield start
        start += step


if __name__ == '__main__':
    print(list(in_range(1, 10, 3)))

