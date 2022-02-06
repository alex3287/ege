# F(35) 1249

def F(n):
    if n < 1:
        return 1
    if n >= 1:
        return 1 + F(n-1) + F(n-2) + 1

# F(35)
print(F(35))