# This code is still not working, have to correct/check this
def partition(a, si, ei):
    pivot = a[si]
    # find number of elements smaller than pivot
    c = 0
    for i in range(si, ei+1):
        if a[i] < pivot:
            c = c+1
    a[si + c], a[si] = a[si], a[si+c]
    pivot_index = si + c

    i = si
    j = ei
    while i < j:
        if (a[i] < pivot):
            i = i+1
        elif a[j] >= pivot:
            j = j-1
        else:
            a[i], a[j] = a[j], a[i]
            i = i+1
            j = j-1
    return pivot_index


def quick_sort(a, si, ei):
    if si >= ei:
        return
    pivot_index = partition(a, si, ei)
    quick_sort(a, si, pivot_index - 1)
    quick_sort(a, pivot_index+1, ei)


a = [1, 2, 3, 4, 5]
print(partition(a, 0, len(a)-1))

print(quick_sort(a, 0, len(a)-1))
