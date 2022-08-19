def first_index(arr, x):
    l = len(arr)
    if l == 0:
        return -1
    if arr[0] == x:
        return 0
    smallerArray = arr[1:]
    smallerListOutput = first_index(smallerArray, x)

    if smallerListOutput == -1:
        return -1
    else:
        return smallerListOutput + 1


def first_index2(arr, x, si):
    l = len(arr)
    if si == l:
        return -1
    if arr[si] == x:
        return si
    smallerListOutput = first_index2(arr, x, si+1)
    return smallerListOutput


arr = [1, 2, 5, 3, 4, 5, 6, 7, 8, 9]

print(first_index(arr, 7))
print(first_index2(arr, 7, 0))
