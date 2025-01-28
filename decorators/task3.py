def arg_rules(type_: type, max_length: int, contains: list):
    def decorator(func):
        def wrapper(arg):
            if not isinstance(arg, type_):
                print(f"Argument is not of type {type_.__name__}")
                return False

            if len(arg) > max_length:
                print(f"Argument exceeds max length of {max_length}")
                return False

            for symbol in contains:
                if symbol not in arg:
                    print(f"Argument does not contain required symbol '{symbol}'")
                    return False

            return func(arg)

        return wrapper
    return decorator


@arg_rules(type_=str, max_length=15, contains=['05', '@'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"


# Tests

assert create_slogan('johndoe05@gmail.com') is False  # Fails max_length
assert create_slogan('S@SH05') == 'S@SH05 drinks pepsi in his brand new BMW!'  # Passes
