import unittest
from build_tree import build_tree
from symmetric import is_symmetric


class TestSym(unittest.TestCase):
    def test1(self):
        arr = [8, 9, 11, 7, 16, 3, 1]
        self.assertEqual(is_symmetric(build_tree(arr)), False)  # add assertion here
    def test2(self):
        arr1 = [3, 8, 8, 9, 6, 6, 9]
        self.assertEqual(is_symmetric(build_tree(arr1)), True)

if __name__ == '__main__':
    unittest.main()
