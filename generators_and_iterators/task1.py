def with_index(iterable, index=0):
    for i in iterable:
        yield index, i
        index += 1


if __name__ == '__main__':
    generator = with_index(["banana", "apple", "grapes"], 5)
    print(next(generator))
    print(next(generator))
    print(next(generator))
