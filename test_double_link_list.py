import unittest
from double_link_list import DoublyLinkedList


class TestDoubleLinkList(unittest.TestCase):
    def test_head_value(self):
        data = DoublyLinkedList(10)
        self.assertEqual(data.head.value, 10)

    def test_print_list(self):
        data = DoublyLinkedList(10)
        self.assertEqual(data.print_list(), [10])

    def test_length(self):
        data = DoublyLinkedList(10)
        self.assertEqual(data.link_list_length(), 1)

    def test_append(self):
        data = DoublyLinkedList(10)
        data.append(5)
        self.assertEqual(data.tail.value, 5)

    def test_pop(self):
        data = DoublyLinkedList(10)
        data.append(5)
        data.append(16)
        data.pop()
        self.assertEqual(data.tail.value, 5)

    def test_prepend(self):
        data = DoublyLinkedList(10)
        data.prepend(5)
        self.assertEqual(data.head.value, 5)

    def test_pop_first(self):
        data = DoublyLinkedList(10)
        data.append(5)
        data.append(16)
        data.pop_first()
        self.assertEqual(data.head.value, 5)

    def test_get(self):
        data = DoublyLinkedList(10)
        data.append(5)
        data.append(16)
        self.assertEqual(data.get(1).value, 5)

    def test_set_value(self):
        data = DoublyLinkedList(10)
        data.append(5)
        data.append(16)
        data.set_value(1, 99)
        self.assertEqual(data.get(1).value, 99)

    def test_insert(self):
        data = DoublyLinkedList(10)
        data.append(5)
        data.append(16)
        data.insert(1, 99)
        self.assertEqual(data.get(1).value, 99)
        self.assertEqual(data.get(2).value, 5)
        self.assertEqual(data.get(3).value, 16)

    def test_remove(self):
        data = DoublyLinkedList(10)
        data.append(5)
        data.append(16)
        data.remove(1)
        self.assertEqual(data.get(1).value, 16)


if __name__ == "__main__":
    unittest.main()
