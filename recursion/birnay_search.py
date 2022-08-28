arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def binarySearch(a, x, si, ei):
    l = len(arr)
    if si > ei:
        return -1
    mid = (si + ei)//2
    if a[mid] == x:
        return mid
    elif a[mid] > x:
        return binarySearch(a, x, si, mid-1)
    else:
        return binarySearch(a, x, mid+1, ei)


pos = binarySearch(arr, 11, 0, 9)
print(pos)
