def twoSum(data, target):
    temp = {}
    for i in data:
        if temp.get(i) == None:
            temp[target - i] = i
        else:
            return [temp[i], i]
    return []
