import unittest
from bin_arr import sort_binary_array as bin

class TestBinArr(unittest.TestCase):
    def test1(self):
        f = [0, 1, 1, 0, 1, 0, 1, 0]
        res = [0, 0, 0, 0, 1, 1, 1, 1]
        self.assertEqual(bin(f), res)  # add assertion here

if __name__ == '__main__':
    unittest.main()
