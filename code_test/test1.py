def fun(n):
    print("fun : ", n)
    if(n == 4):
        print("if : ", n)
        return n
    else:
        print("else : ", n)
        return 2*fun(n+1)


print(fun(2))
