import unittest
from selection_sort import selection_sort


class TestSelectionSort(unittest.TestCase):
    def test_selection_sort(self):
        self.assertEqual(selection_sort([1, 3, 5, 7, 6]), [1, 3, 5, 6, 7])


if __name__ == "__main__":
    unittest.main()
