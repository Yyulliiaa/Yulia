def min_depth(root):
    if root is None:
        return 0
    if root.right is None and root.left is None:
        return 1
    if root.right and root.left:
        return 1 + min (min_depth(root.right), min_depth(root.left))
    if root.left:
        return 1 + min_depth(root.left)
    if root.right:
        return 1 + min_depth(root.right)


