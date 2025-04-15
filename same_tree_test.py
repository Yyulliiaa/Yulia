import unittest
from same_tree import is_same_tree
from build_tree import build_tree as bt


class MyTestCase(unittest.TestCase):
    def test1(self):
        arr = [8, 9, 11, 7, 16, 3, 1]
        self.assertEqual(is_same_tree(bt(arr), bt(arr)), True)  # add assertion here
    def test2(self):
        arr = [8, 9, 11, 7, 16, 3, 1]
        arr1 = [8, 9, 11, 7, 16, 3, 2]
        self.assertEqual(is_same_tree(bt(arr), bt(arr1)), False)
    def test3(self):
        arr = [8, 9, 11, 7, 16, 3, 1]
        arr1 = [8, 9, 11, 7, 16, 3]
        self.assertEqual(is_same_tree(bt(arr), bt(arr1)), False)


if __name__ == '__main__':
    unittest.main()
