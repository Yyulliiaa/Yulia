import unittest
from zero import zero


class TestZero(unittest.TestCase):
    def test1(self):
        f = [0, 0, 1, 0, 3, 12]
        res = [1, 3, 12, 0, 0, 0]
        self.assertEqual(zero(f), res)  # add assertion here

    def test2(self):
        f = [0, 33, 57, 88, 60, 0, 0, 80, 99]
        res = [33, 57, 88, 60, 80, 99, 0, 0, 0]
        self.assertEqual(zero(f), res)

    def test3(self):
        f = [0, 0, 0, 18, 16, 0, 0, 77, 99]
        res = [18, 16, 77, 99, 0, 0, 0, 0, 0]
        self.assertEqual(zero(f), res)

if __name__ == '__main__':
    unittest.main()
