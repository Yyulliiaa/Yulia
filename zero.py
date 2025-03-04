def zero1(arr):
    i = 0
    j = len(arr) - 1
    while i != j:
        if arr[i] == 0:
            arr[j], arr[i] = arr[i], arr[j]
            j -= 1
        i += 1
    return arr

def zero(arr):
    i = 0
    length = len(arr)
    for j in range(length):
        if arr[j] != 0:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    return arr
