def num_in_arr(arr, n):
    length = len(arr)
    small_arr = arr[:length-1]
    if arr[0] == n:
        return True
    present = num_in_arr(small_arr, n)
    return present


li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(num_in_arr(li, 11))
