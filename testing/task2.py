import unittest
from phonebook import *


class TestPhonebook(unittest.TestCase):
    def setUp(self):
        self.demo_phonebook = "demo_phonebook.txt"

    def test_01_create_phonebook(self):
        create_phonebook(self.demo_phonebook)
        self.assertTrue(Path(self.demo_phonebook).exists())

    def test_02_create_contacts(self):
        create_contact(self.demo_phonebook,
                       first_name="Jumapel", last_name="Pisiyk", telephone_number="+3812321312", country="Poland")
        with open(self.demo_phonebook, "r") as file:
            text = file.read()
        self.assertEqual(text, "Jumapel Pisiyk +3812321312 Poland\n")

    def test_03_get_contacts(self):
        result = get_contacts(self.demo_phonebook, "Jumapel")
        self.assertEqual(result, ['Jumapel Pisiyk +3812321312 Poland\n'])

    def test_04_update_contacts(self):
        update_contacts(self.demo_phonebook, "Jumapel", new_first_name="Makar")
        result = get_contacts(self.demo_phonebook, "Makar")
        self.assertEqual(result, ['Makar Pisiyk +3812321312 Poland\n'])

    def test_05_delete_contacts(self):
        delete_contacts(self.demo_phonebook, "Makar")
        result = get_contacts(self.demo_phonebook, "Makar")
        self.assertEqual(result, [])

