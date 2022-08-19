def print_upto_n(n):
    if n == 0:
        return
    print_upto_n(n-1)
    print(n)
    return


print_upto_n(10)


def print_n_to_1(n):
    if n == 0:
        return
    print(n)
    print_n_to_1(n-1)


print_n_to_1(5)
