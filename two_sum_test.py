import unittest
from two_sum import twoSum


class TestSum(unittest.TestCase):
    def test1(self):
        data = [1, 3, 4, 7, 1]
        target = 8
        self.assertEqual(twoSum(data, target), [1, 7])

    def test2(self):
        data = [1, 3, 4, 7, 1]
        target = 1
        self.assertEqual(twoSum(data, target), [])
    def test3(self):
        data = [1, 3, 4, 7, 1]
        target = 51
        self.assertEqual(twoSum(data, target), [])

if __name__ == '__main__':
    unittest.main()
