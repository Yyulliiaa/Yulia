def reverse_array(array, first, last):
    left = first
    right = last
    while left < right:
        array[left], array[right] = array[right], array[left]
        left += 1
        right -= 1
    return array

def reverse_part_of_array(array, part):
    length = len(array)
    part = part % length
    array = reverse_array(array, 0, length - 1)
    array = reverse_array(array, 0, part - 1)
    return reverse_array(array, part, length - 1)