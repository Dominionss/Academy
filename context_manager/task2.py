import unittest
from task1 import MyOpen


class TestMyOpen(unittest.TestCase):
    def setUp(self):
        self.test_file = "test.txt"
        with open(self.test_file, "w", encoding="utf-8") as f:
            f.write("Hello, World!")

    def test_write_to_file(self):
        with MyOpen(self.test_file, "w") as f:
            f.write("New content")

        with open(self.test_file, "r", encoding="utf-8") as f:
            content = f.read()

        self.assertEqual(content, "New content")

    def test_read_from_file(self):
        with MyOpen(self.test_file, "r") as f:
            content = f.read()

        self.assertEqual(content, "Hello, World!")

    def test_non_existent_file(self):
        with self.assertRaises(FileNotFoundError):
            with MyOpen("non_existent.txt", "r") as f:
                f.read()

    def test_file_closing(self):
        with MyOpen(self.test_file, "r") as f:
            self.assertFalse(f.closed)

        self.assertTrue(f.closed)


if __name__ == "__main__":
    unittest.main()
