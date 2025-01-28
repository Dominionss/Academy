def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Function `{func.__name__}` was called with: {args}")
        return func(*args, **kwargs)
    return wrapper


@logger
def add(x, y):
    return x + y


@logger
def square_all(*args):
    return [arg ** 2 for arg in args]


# Tests

add(4, 5)
square_all(1, 2, 3)
