def max_min_multiplication(data):
    if len(data) < 3:
        return -1
    min_ind = 1
    max_ind = 2
    i = 1
    # для бинарного дерева, ветви которого смещены вправо, и все уровни кроме последнего полностью заполнены
    while i < len(data):
        min_ind = i
        i = 2 * i + 1
    i = 0
    while i < len(data):
        max_ind = i
        i = 2 * i + 2
    return data[min_ind] * data[max_ind]

