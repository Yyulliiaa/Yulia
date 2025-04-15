import unittest
from easy_task import copyTime

class TestCopyTime(unittest.TestCase):
    def test1(self):
        self.assertEqual(copyTime(5, 1, 2), 4)


    def test2(self):
        self.assertEqual(copyTime(4, 1, 1), 3)


# add assertion here

if __name__ == '__main__':
    unittest.main()
