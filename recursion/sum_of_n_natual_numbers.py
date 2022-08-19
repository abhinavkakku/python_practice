n = 5


def sum_n(n):
    if n == 0:
        return 0
    temp_out = sum_n(n-1)
    output = temp_out + n
    return output


print(sum_n(5))
