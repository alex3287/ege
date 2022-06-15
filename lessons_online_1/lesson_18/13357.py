def F(n):
    print(n)
    if n >= 3:
        F(n-1)
        F(n-3)


F(5)