import unittest
from merge import merge, merge_sort


class TestMerge(unittest.TestCase):
    def test_merge(self):
        list1 = [1, 3, 5, 7]
        list2 = [2, 4, 6, 8]
        self.assertEqual(merge(list1, list2), [1, 2, 3, 4, 5, 6, 7, 8])

    def test_merge_sort(self):
        list = [8, 4, 2, 7, 5, 1, 3, 6]
        self.assertEqual(merge_sort(list), [1, 2, 3, 4, 5, 6, 7, 8])


if __name__ == "__main__":
    unittest.main()
