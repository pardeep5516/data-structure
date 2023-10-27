import unittest

from stack import Stack


class TestStack(unittest.TestCase):
    def test_stack(self):
        data = Stack(1)
        self.assertEqual(data.top.value, 1)
        self.assertEqual(data.height, 1)

    def test_print_stack(self):
        data = Stack(1)
        self.assertEqual(data.print_stack(), [1])

    def test_push(self):
        data = Stack(1)
        data.push(2)
        self.assertEqual(data.top.value, 2)
        self.assertEqual(data.height, 2)

    def test_pop(self):
        data = Stack(1)
        data.push(2)
        data.push(3)
        data.pop()
        self.assertEqual(data.top.value, 2)
        self.assertEqual(data.height, 2)


if __name__ == "__main__":
    unittest.main()
