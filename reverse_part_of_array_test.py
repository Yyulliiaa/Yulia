import unittest
from reverse_part_of_array import reverse_part_of_array as part_reverse


class TestReversePartOfArray(unittest.TestCase):
    def test1(self):
        self.assertEqual(part_reverse([1, 2, 3, 4, 5, 6, 7], 3), [5, 6, 7, 1, 2, 3, 4])  # add assertion here

    def test2(self):
        self.assertEqual(part_reverse([1, 2, 3, 4, 5, 6, 7], 1), [7, 1, 2, 3, 4, 5, 6])

    def test3(self):
        self.assertEqual(part_reverse([1, 2, 3, 4, 5, 6, 7], 6), [2, 3, 4, 5, 6, 7, 1])

    def test4(self):
        self.assertEqual(part_reverse([1, 2, 3, 4, 5, 6, 7], 7), [1, 2, 3, 4, 5, 6, 7])

    def test5(self):
        self.assertEqual(part_reverse([1, 2, 3, 4, 5, 6, 7], 10), [5, 6, 7, 1, 2, 3, 4])

if __name__ == '__main__':
    unittest.main()
