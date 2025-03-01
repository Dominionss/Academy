from unittest import TestCase
from stack import Stack

class QueueTestCase(TestCase):
    ...

class DequeueTestCase(TestCase):
    ...

class StackTestCase(TestCase):
    def setUp(self):
        self.stack = Stack()
        self.stack._items = [1, 2, 3, 4]

    def _get_stack_size(self):
        return len(self.stack._items)

    def test_stack_is_empty_after_last_item_pop(self):
        stack_length = self._get_stack_size()
        for _ in range(stack_length):
            self.stack.pop()

        self.assertListEqual([], self.stack._items)

    def test_push_adds_element(self):
        """List must contain the same amount of elements as we added..."""
        new_element = 5
        self.stack.push(new_element)
        self.assertEqual(self.stack._items[-1], new_element)

    def test_pop_removes_element(self):
        current_peek = self.stack._items[-1]
        received_element = self.stack.pop()
        self.assertEqual(current_peek, received_element)
        self.assertNotIn(current_peek, self.stack._items)

    def test_peek_gets_the_element_without_removal_from_the_stack(self):
        """When we received peek item it should not be deleted from the stack..."""
        received_element = self.stack.peek()
        self.assertIn(received_element, self.stack._items)
        self.assertEqual(self.stack._items[-1], received_element)

    def test_size_returns_number_of_elements(self):
        stack_length = self._get_stack_size()
        self.assertEqual(stack_length, self.stack.size())
