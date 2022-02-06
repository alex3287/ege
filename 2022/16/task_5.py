def F(n):
    if n <= 0:
        return 0
    if n > 0:
        return F(n-4) + n + F(n // 3)


print(F(67))
