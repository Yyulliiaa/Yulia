import unittest
from max_min_mult import max_min_multiplication as mmm



class Test(unittest.TestCase):
    def test1(self):
        arr = [16, 14, 18, 11, 15, 17, 24]
        self.assertEqual(mmm(arr), 264)  # add assertion here


if __name__ == '__main__':
    unittest.main()
