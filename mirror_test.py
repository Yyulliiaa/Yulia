import unittest
from mirror import count_mirror_twins as count
class TreeNode:
    def __init__ (self, val = 0, left = None, right = None):
        self.data = val
        self.left = left
        self.right = right

class MyTestCase(unittest.TestCase):
    def test1(self):
        root = TreeNode(3)
        root.left = TreeNode(9)
        root.right= TreeNode(9)
        root.left.left = TreeNode(6)
        root.left.right = TreeNode(8)
        root.right.left = TreeNode(8)
        root.right.right = TreeNode(6)
        self.assertEqual(count(root),  3)  # add assertion here
    def test2(self):
        root = TreeNode(3)
        root.left = TreeNode(9)
        root.right= TreeNode(9)
        root.left.left = TreeNode(6)
        root.right.left = TreeNode(6)
        self.assertEqual(count(root),  1)


if __name__ == '__main__':
    unittest.main()
