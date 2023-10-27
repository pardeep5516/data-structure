import unittest
from queue import Queue


class TestQueue(unittest.TestCase):
    def test_queue(self):
        data = Queue(1)
        self.assertEqual(data.first.value, 1)
        self.assertEqual(data.last.value, 1)
        self.assertEqual(data.length, 1)

    def test_enquue(self):
        data = Queue(1)
        data.enqueue(2)
        self.assertEqual(data.first.value, 1)
        self.assertEqual(data.last.value, 2)
        self.assertEqual(data.length, 2)

    def test_dequeue(self):
        data = Queue(1)
        data.enqueue(2)
        data.enqueue(3)
        data.dequeue()
        self.assertEqual(data.first.value, 2)
        self.assertEqual(data.last.value, 3)
        self.assertEqual(data.length, 2)


if __name__ == "__main__":
    unittest.main()
