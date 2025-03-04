def merge_sorted_arrays(arr1, arr2):
    merged_array = []
    len1 = len(arr1)
    len2 = len(arr2)
    if is_sorted(arr1, len1) & is_sorted(arr2, len2) != 1:
        return merged_array
    i, j = 0, 0
    while i < len1 and j < len2:
        if arr1[i] < arr2[j]:
            merged_array.append(arr1[i])
            i += 1
        else:
            merged_array.append(arr2[j])
            j += 1
    merged_array += arr1[i:]
    merged_array += arr2[j:]
    return merged_array

def is_sorted(arr, size):
    if size <= 1:
        return True
    for i in range(1, size - 1):
        if arr[i - 1] > arr[i]:
            return False
    return True