import unittest
from sqrt import binarySearchSqrt as sq


class TestSqrt(unittest.TestCase):
    def test1(self):
        self.assertEqual(sq(16), 4)

    def test2(self):
        self.assertEqual(sq(17), 4)

    def test3(self):
        self.assertEqual(sq(15), 3)

if __name__ == '__main__':
    unittest.main()