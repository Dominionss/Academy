import unittest
from collections.abc import Iterable
from generators_and_iterators import *


class TestGeneratorsAndIterators(unittest.TestCase):
    def setUp(self):
        self.mylist = MyList(["banana", "apple", "orange", "grapes", "pineapple"])
        self.generator = with_index(self.mylist)
        self.iterator = in_range(1, 10, 3)

    def test_with_index(self):
        self.assertEqual(next(self.generator), (0, "banana"))
        self.assertEqual(next(self.generator), (1, "apple"))
        self.assertEqual(next(self.generator), (2, "orange"))
        self.assertEqual(next(self.generator), (3, "grapes"))
        self.assertEqual(next(self.generator), (4, "pineapple"))
        self.assertRaises(StopIteration, next, self.generator)

    def test_in_range(self):
        self.assertEqual(next(self.iterator), 1)
        self.assertEqual(next(self.iterator), 4)
        self.assertEqual(next(self.iterator), 7)
        self.assertEqual(next(self.iterator), 10)
        self.assertRaises(StopIteration, next, self.iterator)

    def test_mylist(self):
        self.assertEqual(self.mylist[0], "banana")
        self.mylist[0] = "cake"
        self.assertEqual(self.mylist[0], "cake")
        self.assertNotIn("banana", self.mylist)
        self.assertIn("pineapple", self.mylist)
        self.mylist.append("pumpkin")
        self.assertEqual(self.mylist[-1], "pumpkin")
        self.assertEqual(len(self.mylist), 6)
        del self.mylist[0]
        self.assertEqual(len(self.mylist), 5)
        self.assertTrue(isinstance(self.mylist, Iterable), True)
