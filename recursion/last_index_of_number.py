def last_index(arr, x):
    l = len(arr)
    if l == 0:
        return -1

    smallerList = arr[1:]
    smallerListOutput = last_index(smallerList, x)
    if smallerListOutput != -1:
        return smallerListOutput+1
    else:
        if arr[0] == x:
            return 0
        else:
            return -1


def last_index2(arr, x, si):
    l = len(arr)
    if si == l:
        return -1
    smallerListOutput = last_index2(arr, x, si+1)
    if smallerListOutput != -1:
        return smallerListOutput
    else:
        if arr[si] == x:
            return si
        else:
            return -1


arr = [1, 2, 3, 4, 5, 6, 7, 7, 9, 10]
print(last_index(arr, 7))
print(last_index2(arr, 3, 0))
