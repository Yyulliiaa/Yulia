import unittest
from two_sum import two_sum


class TestTwoSum(unittest.TestCase):
    def test_empty(self):
        res = two_sum([], 1)
        self.assertEqual(len(res), 0, "пустой массив")  # add assertion here

    def test_sorted(self):
        res = two_sum([9, 9, -1, 10], 1)
        self.assertEqual(len(res), 0, "массив не отсортирован")

    def test_all_rigth(self):
        res = two_sum([3, 8, 9, 11, 16, 18, 19, 21], 25)
        self.assertEqual(res,[2, 4], "2, 4")

    def test_impossible(self):
        res = two_sum([3, 8, 10, 11, 16, 18, 19, 21], 25)
        self.assertEqual(len(res), 0, "не найдено")

if __name__ == '__main__':
    unittest.main()
