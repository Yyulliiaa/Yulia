def dept_search(root, res):
    if root is None:
        return res
    dept_search(root.left, res)
    res.append(root.data)
    dept_search(root.right, res)
    return res


def is_symmetric_dfs(root):
    if root is None:
        return True
    data = []
    data = dept_search(root, data)
    j = len(data) - 1
    for i in range(len(data) // 2):
        if data[i] != data[j]:
            return False
        j -= 1
    return True
