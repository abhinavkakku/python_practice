def array_sum(a, N):
    if N <= 0:
        return 0
    else:
        return (array_sum(a, N-1) + a[N-1])


list1 = [1, 2, 3, 4, 6]
l = len(list1)
print(l)
print(array_sum(list1, l))
