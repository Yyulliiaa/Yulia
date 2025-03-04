import unittest
from reverse_array import reverse_array


class TestReverseArray(unittest.TestCase):
    def test1(self):
        self.assertEqual(reverse_array([3, 8, 6, 9, 9, 8, 6]), [6, 8, 9, 9, 6, 8, 3])  # add assertion here


if __name__ == '__main__':
    unittest.main()
