import unittest
from even import even_shift as ev

class TestEven(unittest.TestCase):
    def test1(self):
        f = [3, 2, 4, 1, 11, 8, 9]
        res = [2, 4, 8, 1, 11, 3, 9]
        self.assertEqual(ev(f), res)


if __name__ == '__main__':
    unittest.main()
