def binarySearchSqrt(target):
    l = 0
    r = target
    while l <= r :
        middle = (l + r) // 2
        if middle ** 2 > target:
            r = middle - 1
        elif middle ** 2 < target:
            l = middle + 1
        else:
            return middle
    return r
