def F(n):
    if n <= 1:
        return n * n
    return (n*n) + (2*n+1) + F(n-2) + F(n // 3)


for i in range(210):
    if F(i) > 3200000:
        print(i, '->', F(i))
        break