"""
square_nums (takes a list of integers and returns the list of squares)
remove_positives (takes a list of integers and returns it without positive numbers
filter_leaps (takes a list of dates (integers) and removes those that are not 'leap years'
"""

class Mathematician:
    def square_nums(self, numbers: list):
        square_number = lambda x: x ** 2
        numbers = list(map(square_number, numbers))
        return numbers

    def remove_positives(self, numbers: list):
        negative_number = lambda x: True if x < 0 else False
        numbers = list(filter(negative_number, numbers))
        return numbers

    def filter_leaps(self, dates: list):
        return [x for x in dates if x % 4 == 0 and (x % 100 != 0 or x % 400 == 0)]


mathematician = Mathematician()

print(mathematician.square_nums([7, 11, 5, 4])) # == [49, 121, 25, 16]

print(mathematician.remove_positives([26, -11, -8, 13, -90])) # == [-11, -8, -90]

print(mathematician.filter_leaps([2001, 1884, 1995, 2003, 2020])) # == [1884, 2020
