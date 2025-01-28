class Dog:
    age_factor = 7

    def __init__(self, age):
        self.age = age

    def human_age(self):
        return self.age * Dog.age_factor


# Tests

dog = Dog(3)
print(f"The dog's age in human equivalent is: {dog.human_age()} years.")
