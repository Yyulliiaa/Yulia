import unittest
from color import sort_color


class TestColorArr(unittest.TestCase):
    def test1(self):
        f = [2, 0, 2, 1, 1, 0]
        res = [0, 0, 1, 1, 2, 2]
        self.assertEqual(sort_color(f), res)  # add assertion here


if __name__ == '__main__':
    unittest.main()
