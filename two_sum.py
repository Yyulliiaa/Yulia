def two_sum(sorted_array, target):
    if not sorted_array:
        return []
    length = 0
    i = sorted_array[0]
    for j in sorted_array:
        length += 1
        if i > j:
            return []
        i = j
    left = 0
    right = length - 1
    while left != right:
        res = sorted_array[left] + sorted_array[right]
        if res == target:
            return [left, right]
        if res > target:
            right -= 1
        else:
            left += 1
    return []

