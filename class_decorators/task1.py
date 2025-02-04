import re


class User:
    def __init__(self, email: str):
        self.validate(email)
        self.email = email

    @classmethod
    def validate(cls, email: str):
        pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        if not re.match(pattern, email):
            raise ValueError(f"Invalid email address: {email}")


if __name__ == '__main__':
    user1 = User('sdkjfbkjafd@gmail.com')
    user2 = User('sjafbsfbasdf@catmail.com')
    user3 = User('sdfsafsfd')
