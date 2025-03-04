import unittest
from union2 import merge_sorted_arrays as merge


class TestUnion2(unittest.TestCase):
    def test1(self):
        f = [3, 8, 10, 11]
        s = [1, 7, 9]
        res = [1, 3, 7, 8, 9, 10, 11]
        self.assertEqual(merge(f, s), res)  # add assertion here

    def test_not_sorted(self):
        f = [90, 8, 10, 11]
        s = [1, 7, 9]
        res = []
        self.assertEqual(merge(f, s), res)


if __name__ == '__main__':
    unittest.main()
