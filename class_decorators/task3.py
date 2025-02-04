from functools import wraps


class TypeDecorators:
    @staticmethod
    def to_int(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            return int(func(*args, **kwargs))
        return wrapper

    @staticmethod
    def to_str(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            return str(func(*args, **kwargs))
        return wrapper

    @staticmethod
    def to_bool(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            return bool(func(*args, **kwargs))
        return wrapper

    @staticmethod
    def to_float(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            return float(func(*args, **kwargs))
        return wrapper


if __name__ == '__main__':
    @TypeDecorators.to_int
    def do_nothing(string: str):
        return string


    @TypeDecorators.to_bool
    def do_something(string: str):
        return string

    print(do_nothing('25') == 25)
    print(do_something('True') is True)
