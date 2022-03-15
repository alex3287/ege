with open('input.txt') as fin:
    A = []
    for i in range(500):
        n = fin.readline().replace(',', '.')
        A.append(float(n))
print(A)

sum_max = 0
suma = A[0]
for i in range(len(A)-1):
    if suma < 0:
        suma = 0
    if abs(A[i] - A[i+1]) <= 8:
        suma += A[i+1]
        if suma > sum_max:
            sum_max = suma
    else:
        suma = A[i+1]

print(sum_max)