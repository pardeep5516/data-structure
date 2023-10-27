import unittest
from factorial import factorial


class TestFactorial(unittest.TestCase):
    def test_factorial(self):
        self.assertEqual(factorial(5), 120)


if __name__ == "__main__":
    unittest.main()
