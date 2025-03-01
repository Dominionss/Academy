import unittest
import random


def linear_search(array, target):
    """Search for a target item in an array by taking elements one by one."""
    _types = (list, tuple, str)
    if not isinstance(array, _types):
        raise TypeError('Array is not a list or tuple or str.')
    x = 0
    for element in array:
        if element == target:
            return x
        x += 1

class LinearSearchTestCase(unittest.TestCase):
    def setUp(self):
        random.seed(555)
        self.random_numbers = [random.randint(1, 100) for x in range(0, 99)]
        self.target_item = 115
        self.expected_index = 57
        self.random_numbers.insert(self.expected_index, self.target_item)

    def test_returns_correct_items_index(self):
        result = linear_search(self.random_numbers, self.target_item)
        self.assertEqual(result, self.expected_index)

    def test_accepted_data_types(self):
        # self.assertRaises(TypeError, linear_search, 1, 1)
        # linear_search(1, 1)
        with self.assertRaises(TypeError):
            linear_search(1, 1)

if __name__ == '__main__':
    unittest.main()


