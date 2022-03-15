def f(number):
    return number-3, number+4


B = []
A = [1]
for i in range(7):
    for j in A:
        x, y = f(j)
        B.append(x)
        B.append(y)
    A = list(set(B))
    B = []

print(len(A))

