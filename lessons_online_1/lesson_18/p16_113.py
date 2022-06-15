def F(n):
    if n == 0:
        return 0
    if n > 0 and n % 2 == 0:
        return F(n / 2) - 1
    if n > 0 and n % 2 == 1:
        return 3 + F(n-1)


A = []
for i in range(1000):
    temp = F(i)
    if temp not in A:
        A.append(temp)

print(A, len(A))