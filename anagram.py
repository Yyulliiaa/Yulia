def anagram(array):
    big = {}
    for i in range(len(array)):
        big[i] = {}
        for j in array[i]:
            if big[i].get(j, 1):
                big[i][j] = 0
            big[i][j] += 1
    res = [0 for _ in range(len(array))]
    k = 0
    for i in range(len(array)):
        one = big[i]
        if res[i] == 0:
            k += 1
            res[i] = k
            for j in range(i + 1, len(array)):
                if res[j] == 0:
                    two = big[j]
                    flag = 1
                    for key in one.keys():
                        if  not two.get(key):
                            flag = 0
                            break
                    if flag:
                        res[j] = k
    res1 = [[] for _ in range (k)]
    for i in range(len(array)):
        res1[res[i] - 1].append(array[i])
    return res1



array = ["eat", "tea", "tan", "ate", "nat", "bat"]
have = anagram(array)
print(have)

array1 = ["won", "now", "aaa", "ooo", "ooo"]
have = anagram(array1)
print(have)
