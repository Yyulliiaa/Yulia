import unittest
from extra_letter import extraLetter

class TestString(unittest.TestCase):
    def test1(self):
        a = "uio"
        b = "oeiu"
        self.assertEqual(extraLetter(a, b), "e")  # add assertion here
    def test2(self):
        a = "fe"
        b = "efo"
        self.assertEqual(extraLetter(a, b), "o")
    def test3(self):
        a = "ab"
        b = "ab"
        self.assertEqual(extraLetter(a, b), "")
    def test4(self):
        a = "bbb"
        b = "bbbb"
        self.assertEqual(extraLetter(a, b), "b")


if __name__ == '__main__':
    unittest.main()
