class Animal:
    def talk(self):
        raise NotImplementedError("Subclasses must implement the talk method")


class Dog(Animal):
    def talk(self):
        return "gav gav"


class Cat(Animal):
    def talk(self):
        return "meow meow"


dog = Dog()
cat = Cat()
print(dog.talk())
print(cat.talk())
