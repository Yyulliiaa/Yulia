def extraLetter(a, b):
    map = {}
    for i in b:
        if map.get(i) == None:
            map[i] = 0
        map[i] += 1
    for i in a:
        map[i] -= 1
    for i in map.items():
        if i[1] == 1:
            return i[0]
    return ""
