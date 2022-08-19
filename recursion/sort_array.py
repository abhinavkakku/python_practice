def isSorted(a):
    l = len(a)
    if l == 0 or l == 1:
        return True
    if a[0] > a[1]:
        return False
    smallerList = a[1:]
    isSmallerListSorted = isSorted(smallerList)
    if isSmallerListSorted:
        return True
    else:
        return False


def isSorted2(arr, si):
    l = len(arr)
    if si == l or si == l-1:
        return True
    if a[si] > a[si + 1]:
        return False
    issmallerPartSorted = isSorted2(a, si+1)
    return issmallerPartSorted


a = [1, 2, 3, 3, 5]

print(isSorted(a))

print(isSorted2(a, 0))
