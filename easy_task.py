import math

def copyTime (n, x, y):
    minim = min(x, y)
    l = 0
    r = (n - 1) * minim
    while l + 1 < r:
        mid = (r - l + 1) / 2
        if (r // x +  r // y) >= n - 1:
            r = mid
        else:
            l = mid
    return math.ceil(r) + minim
