# тут нужно еще работать, алгоритм не совсем верен
A = open('input.txt').readline()
k = 0
k_max = 0
d = 0
for i in range(0, len(A)):
    if (A[i] == 'D' and d < 1) or A[i] != 'D':
        if A[i] != "D":
            k += 1
            if k >= k_max:
                k_max = k
        if A[i] == 'D' and d < 1:
            d += 1
            k += 1
    else:
        k = 0
        d = 0

print(k_max)
