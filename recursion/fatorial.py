import sys
sys.setrecursionlimit(7000)


def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)


print(factorial(2900))
