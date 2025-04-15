import unittest
from build_tree import build_tree
from min_depth import min_depth


class TestSym(unittest.TestCase):
    def test1(self):
        arr = [8, 9, 11, 7, 16, 3, 1]
        self.assertEqual(min_depth(build_tree(arr)), 3)  # add assertion here
    def test2(self):
        arr1 = [3, 8, 8, 9, 6]
        self.assertEqual(min_depth(build_tree(arr1)), 2)

if __name__ == '__main__':
    unittest.main()
