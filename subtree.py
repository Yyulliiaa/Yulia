from same_tree import is_same_tree

def is_subtree(a, b):
    if b is None:
        return True
    if a is None:
        return False
    if is_same_tree(a, b):
        return True
    return is_same_tree(a.left, b) | is_same_tree(a.right, b)