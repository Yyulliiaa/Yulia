def even_shift(arr):
    i, even = 0, 0
    length = len(arr)
    while i < length:
        if arr[i] % 2 == 0:
            arr[even], arr[i] = arr[i], arr[even]
            even += 1
        i += 1
    return arr

