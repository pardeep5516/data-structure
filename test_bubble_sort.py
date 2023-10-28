import unittest
from bubble_sort import bubble_sort


class TestBubbleSort(unittest.TestCase):
    def test_bubble_sort(self):
        self.assertEqual(bubble_sort([1, 2, 5, 7, 6]), [1, 2, 5, 6, 7])


if __name__ == "__main__":
    unittest.main()
