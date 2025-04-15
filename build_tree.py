class TreeNode:
    def __init__ (self, val = 0, left = None, right = None):
        self.data = val
        self.left = left
        self.right = right

    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.data)
        if self.right:
            self.right.print_tree()



def build_tree(array, i = 0):
    if i >= len(array):
        return None
    root = TreeNode(array[i])
    root.left = build_tree(array, 2 * i + 1)
    root.right = build_tree(array, 2 * i + 2)
    return root





arr = [8, 9, 11, 7, 16, 3, 1]
build_tree(arr)