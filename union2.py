def merge_sorted_arrays(arr1, arr2):
    len1 = len(arr1)
    len2 = len(arr2)
    if is_sorted(arr1, len1) & is_sorted(arr2, len2) != 1:
        return []
    arr1 += [0 for _ in range(len2)]
    i = len1 - 1
    j = len2 - 1
    k = len2 + len1 - 1
    while j >= 0:
        if i >= 0 and arr1[i] > arr2[j]:
            arr1[k] = arr1[i]
            i -= 1
        else:
            arr1[k] = arr2[j]
            j -= 1
        k -= 1
    return arr1

def is_sorted(arr, size):
    if size <= 1:
        return True
    for i in range(1, size - 1):
        if arr[i - 1] > arr[i]:
            return False
    return True

