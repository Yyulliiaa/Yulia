import unittest
from feed_animal import feedAnimals


class TestFood(unittest.TestCase):
    def test1(self):
        food = [1, 4, 3, 8]
        animals = [8, 2, 3, 2]
        self.assertEqual(feedAnimals(animals, food), 3)  # add assertion here

    def test2(self):
        animals = [1, 2, 3, 4, 8]
        food = [8, 3, 9, 1, 7]
        self.assertEqual(feedAnimals(animals, food), 5)
    def test3(self):
        animals = [1, 2, 3, 4, 8]
        food = [ 3, 9, 1, 1]
        self.assertEqual(feedAnimals(animals, food), 3)


if __name__ == '__main__':
    unittest.main()
