import unittest
from binary_tree import BinarySearchTree


class TestBST(unittest.TestCase):
    def test_insert(self):
        bst = BinarySearchTree()
        bst.insert(10)
        bst.insert(5)
        bst.insert(15)
        self.assertEqual(bst.root.value, 10)
        self.assertEqual(bst.root.left.value, 5)
        self.assertEqual(bst.root.right.value, 15)

    def test_contains(self):
        bst = BinarySearchTree()
        bst.insert(10)
        bst.insert(5)
        bst.insert(15)
        self.assertTrue(bst.contains(10))
        self.assertTrue(bst.contains(5))
        self.assertTrue(bst.contains(15))
        self.assertFalse(bst.contains(20))


if __name__ == "__main__":
    unittest.main()
