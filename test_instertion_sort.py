import unittest
from insertion_sort import insertion_sort


class TestInsertionSort(unittest.TestCase):
    def test_insertion_sort(self):
        self.assertEqual(insertion_sort([1, 3, 5, 7, 6]), [1, 3, 5, 6, 7])


if __name__ == "__main__":
    unittest.main()
